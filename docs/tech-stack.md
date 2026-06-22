# Tech Stack

What runs under the hood.

## Operating System

- **OS:** Ubuntu 24.04 LTS
- **Kernel:** 6.x series

## Container Runtime

- **Docker** with **containerd**
- Composed stacks managed via **CasaOS** (self-hosted app platform)

## Web Server

- **nginx** — reverse proxy and static file server

## Hermes Agent

- **Hermes** by Nous Research — autonomous AI agent framework
- Providers: OpenRouter, Gemini, OpenCode
- Connected platforms: Telegram, ntfy, REST API
- 8 cron jobs: health monitoring, daily briefings, research, session management, backup

## Networking

- **Cloudflare** — DNS, proxy, DDoS protection, TLS
- **Cloudflare Tunnel** — secure ingress for private services
- **nginx** — subdomain routing and reverse proxying

## Databases

- **PostgreSQL 14** — Nextcloud database
- **Redis 6** — Nextcloud caching
- **SQLite** — various apps (FreshRSS, FileBrowser, PiGallery2)

## Storage & Sync

- **Samba** — local network file sharing
- **Syncthing** — P2P device sync (phone, laptop, server)

## Monitoring & Automation

- **Hermes Agent cron** — 8 automated jobs (watchdog, health reports, daily briefings, session management)
- **System cron** — daily backups at 4am
- **Ntfy** — push notification delivery to phone

## Development

- Node.js
- Python 3
- Shell scripting (Bash)
- Git / GitHub

## Hardware

A custom-built PC running 24/7 at home. SSD storage, NVIDIA GPU, wired ethernet connection.
