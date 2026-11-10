import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

export const runtime = 'nodejs';

const DATA_DIR = path.join(process.cwd(), 'data');
const USERS_FILE = path.join(DATA_DIR, 'user_store.json');
const CHATS_FILE = path.join(DATA_DIR, 'chat_history.json');

async function atomicWriteFile(filePath: string, data: string) {
  const tmpFile = `${filePath}.${Date.now()}.${Math.random().toString(36).slice(2)}.tmp`;
  await fs.writeFile(tmpFile, data, 'utf-8');
  await fs.rename(tmpFile, filePath);
}

async function ensureDataFiles() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true });
  } catch {
    // directory already exists
  }

  try {
    await fs.access(USERS_FILE);
  } catch {
    await atomicWriteFile(USERS_FILE, JSON.stringify({ users: [] }, null, 2));
  }

  try {
    await fs.access(CHATS_FILE);
  } catch {
    await atomicWriteFile(CHATS_FILE, JSON.stringify({ chats: {} }, null, 2));
  }
}

function isValidId(id: unknown): id is string {
  return (
    typeof id === 'string' &&
    id.length > 0 &&
    id !== '__proto__' &&
    id !== 'constructor' &&
    id !== 'prototype'
  );
}

export async function GET(req: NextRequest) {
  try {
    await ensureDataFiles();
    const { searchParams } = new URL(req.url);
    const type = searchParams.get('type');
    const userId = searchParams.get('userId');

    if (type === 'users') {
      const data = await fs.readFile(USERS_FILE, 'utf-8');
      const parsed = JSON.parse(data || '{"users":[]}');
      // Sanitize: never return password hashes in public GET requests
      const sanitizedUsers = (parsed.users || []).map(
        (u: { id?: string; name?: string; email?: string; avatar_url?: string; created_at?: string }) => ({
          id: u.id,
          name: u.name,
          email: u.email,
          avatar_url: u.avatar_url,
          created_at: u.created_at,
        })
      );
      return NextResponse.json({ users: sanitizedUsers });
    }

    if (type === 'chats' && isValidId(userId)) {
      const data = await fs.readFile(CHATS_FILE, 'utf-8');
      const parsed = JSON.parse(data || '{"chats":{}}');
      return NextResponse.json({ conversations: parsed.chats[userId] || [] });
    }

    return NextResponse.json({ status: 'ok' });
  } catch (error: unknown) {
    const message = (error as Error)?.message || 'Failed to read storage';
    return NextResponse.json({ error: message }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    await ensureDataFiles();
    const body = await req.json();
    const { type, user, userId, conversations } = body;

    if (type === 'sync_user' && user && isValidId(user.id)) {
      const raw = await fs.readFile(USERS_FILE, 'utf-8');
      const store = JSON.parse(raw || '{"users":[]}');
      const existingIdx = store.users.findIndex(
        (u: { id?: string; email?: string }) => u.id === user.id || (user.email && u.email === user.email)
      );

      if (existingIdx >= 0) {
        store.users[existingIdx] = { ...store.users[existingIdx], ...user };
      } else {
        store.users.push(user);
      }

      await atomicWriteFile(USERS_FILE, JSON.stringify(store, null, 2));
      return NextResponse.json({ success: true, user });
    }

    if (type === 'sync_chats' && isValidId(userId) && Array.isArray(conversations)) {
      const raw = await fs.readFile(CHATS_FILE, 'utf-8');
      const store = JSON.parse(raw || '{"chats":{}}');
      store.chats[userId] = conversations;

      await atomicWriteFile(CHATS_FILE, JSON.stringify(store, null, 2));
      return NextResponse.json({ success: true });
    }

    return NextResponse.json({ error: 'Invalid payload type or userId' }, { status: 400 });
  } catch (error: unknown) {
    const message = (error as Error)?.message || 'Failed to write storage';
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
