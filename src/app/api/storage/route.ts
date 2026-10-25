import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

export const runtime = 'nodejs';

const DATA_DIR = path.join(process.cwd(), 'data');
const USERS_FILE = path.join(DATA_DIR, 'user_store.json');
const CHATS_FILE = path.join(DATA_DIR, 'chat_history.json');

async function ensureDataFiles() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true });
  } catch {
    // directory already exists
  }

  try {
    await fs.access(USERS_FILE);
  } catch {
    await fs.writeFile(USERS_FILE, JSON.stringify({ users: [] }, null, 2), 'utf-8');
  }

  try {
    await fs.access(CHATS_FILE);
  } catch {
    await fs.writeFile(CHATS_FILE, JSON.stringify({ chats: {} }, null, 2), 'utf-8');
  }
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
      return NextResponse.json(parsed);
    }

    if (type === 'chats' && userId) {
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

    if (type === 'sync_user' && user) {
      const raw = await fs.readFile(USERS_FILE, 'utf-8');
      const store = JSON.parse(raw || '{"users":[]}');
      const existingIdx = store.users.findIndex((u: { id?: string; email?: string }) => u.id === user.id || u.email === user.email);

      if (existingIdx >= 0) {
        store.users[existingIdx] = { ...store.users[existingIdx], ...user };
      } else {
        store.users.push(user);
      }

      await fs.writeFile(USERS_FILE, JSON.stringify(store, null, 2), 'utf-8');
      return NextResponse.json({ success: true, user });
    }

    if (type === 'sync_chats' && userId && Array.isArray(conversations)) {
      const raw = await fs.readFile(CHATS_FILE, 'utf-8');
      const store = JSON.parse(raw || '{"chats":{}}');
      store.chats[userId] = conversations;

      await fs.writeFile(CHATS_FILE, JSON.stringify(store, null, 2), 'utf-8');
      return NextResponse.json({ success: true });
    }

    return NextResponse.json({ error: 'Invalid payload type' }, { status: 400 });
  } catch (error: unknown) {
    const message = (error as Error)?.message || 'Failed to write storage';
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
