# Apps

All the self-hosted apps running on my server. Every one is open source and runs in Docker.

---

## Nextcloud — Cloud Storage

My personal Dropbox. Files, photos, contacts, calendar — all self-hosted. Uses PostgreSQL for the database and Redis for caching. Has a cron job that runs nightly maintenance.

**What I use it for:** Syncing files between devices, sharing large files with friends, backing up phone photos automatically.

---

## SearXNG — Private Search Engine

A meta-search engine that queries multiple backends (Google, DuckDuckGo, Wikipedia, etc.) and returns results without tracking you. No logs, no profiling, no ads.

**What I use it for:** Searching the web without being the product.

---

## FreshRSS — RSS Reader

Fetches and displays RSS feeds from websites and blogs I follow. Has a great mobile app (FeedMe) that connects to it.

**What I use it for:** Staying up to date with blogs, news sites, and content creators without algorithmic feeds.

---

## Homepage — Dashboard

A clean, customizable startpage that shows all my services in one place. Auto-discovers running Docker containers and shows their status.

**What I use it for:** A browser homepage with quick access to everything.

---

## Obsidian — Notes

My note-taking app, running in a container so I can access it from any browser. Syncs across devices via Syncthing.

**What I use it for:** All my notes, journaling, project planning. Hermes Agent also writes to my vault automatically.

---

## Ntfy — Push Notifications

Sends push notifications to my phone. Simple HTTP API — any script or automation can send me a ping.

**What I use it for:** Hermes cron jobs send me alerts (server health issues, daily briefings). My own scripts use it too.

---

## Syncthing — File Sync

Decentralized file synchronization. No cloud, no central server — devices sync directly peer-to-peer.

**What I use it for:** Keeping my Obsidian vault, photos, and documents in sync across phone, laptop, and server.

---

## PiGallery2 — Photo Gallery

A beautiful self-hosted photo gallery. Scans photo directories and generates thumbnails automatically.

**What I use it for:** Browsing and sharing my photo collection.

---

## Portainer — Docker Manager

Web UI for managing Docker containers, images, volumes, and networks.

**What I use it for:** Quick container troubleshooting without SSH-ing.

---

## FileBrowser

A simple web-based file manager. Upload, download, delete, and preview files from any browser.

**What I use it for:** Quick file management without needing to SSH in.

---

## Epic Games Claimer

Automatically claims free games from the Epic Games Store so I never miss one. Runs on a schedule and notifies me when it claims something.

**What I use it for:** Growing my game library without remembering to check the store.

---

## Hermes Workspace

A browser-based development environment with a code editor and terminal. Accessible from any device with a browser.

**What I use it for:** Quick code edits and scripting on the go.

---

## Hermes Agent — AI Assistant

My autonomous AI agent (powered by Nous Research's Hermes). It runs on the server 24/7 and automates tasks for me — monitoring, reporting, research, content generation. It connects to Telegram so I can talk to it from my phone.

**What I use it for:** Morning briefings, server health monitoring, automated research, note-taking, and way too many other things.
