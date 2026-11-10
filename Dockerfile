# Production image for AgriVision (Next.js standalone runtime)
# Based on https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile

ARG NODE_VERSION=22-alpine

# ============================================
# Stage 1: Install dependencies
# ============================================
FROM node:${NODE_VERSION} AS dependencies

RUN apk add --no-cache libc6-compat
WORKDIR /app

# Copy manifest + lockfile first to leverage Docker layer caching
COPY package.json package-lock.json ./

# Frozen lockfile for reproducible builds; skip Playwright's browser download
RUN PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm ci --no-audit --no-fund

# ============================================
# Stage 2: Build the Next.js app (standalone output)
# ============================================
FROM node:${NODE_VERSION} AS builder

RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY --from=dependencies /app/node_modules ./node_modules
COPY . .

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
# Limit V8 heap during build to avoid OOM crash on 1GB - 2GB VPS
ENV NODE_OPTIONS="--max-old-space-size=1536"

RUN npm run build

# ============================================
# Stage 3: Slim runtime
# ============================================
FROM node:${NODE_VERSION} AS runner

RUN apk add --no-cache libc6-compat
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"
ENV NEXT_TELEMETRY_DISABLED=1

# Pre-create app data and .next directories and assign ownership to node user
RUN mkdir -p /app/data /app/.next && chown -R node:node /app/data /app/.next

# Copy public assets and core pathology database
COPY --from=builder --chown=node:node /app/public ./public
COPY --from=builder --chown=node:node /app/src/data ./src/data

# Copy Next.js standalone server and static assets
COPY --from=builder --chown=node:node /app/.next/standalone ./
COPY --from=builder --chown=node:node /app/.next/static ./.next/static

# Non-root for security
USER node

EXPOSE 3000

CMD ["node", "server.js"]
