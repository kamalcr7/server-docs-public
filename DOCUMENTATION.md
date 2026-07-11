# Kamal's Server — Public Docs

## Quick Summary

A sanitized, public-friendly version of the KamalServer documentation. Showcases the home server's architecture, apps, projects, and tech stack at a high level — without sensitive details like config values, ports, or recovery procedures. Deployed to `server-docs-public.pages.dev` via Cloudflare Pages.

## 30-Second Explanation

This is the public-facing version of Kamal's home server documentation. Unlike the private repo (`server-docs`), this version omits all sensitive operational details (config files, env vars, backup procedures) and presents a curated overview of:
- **What the server runs** — 14 Docker containers, game servers, AI agent
- **What projects are built on it** — BlockOps FPS, Retro Arcade, Hermes integration, backup automation
- **The tech stack** — Linux Mint, Docker, CasaOS, nginx, Cloudflare, Node.js, Python, and more
- **How everything connects** — Cloudflare Tunnel → nginx → containers/services

It uses MkDocs Material with custom CSS for a clean, card-based visual design. Deployed via Cloudflare Pages with multiple deploy scripts (Python direct upload, bash, wrangler).

## Tech Stack

| Layer | Technology |
|---|---|
| Documentation Engine | MkDocs with Material theme |
| Diagrams | Mermaid.js |
| Plugins | `search` |
| Custom CSS | `extra.css` |
| Fonts | Inter (text), JetBrains Mono (code) |
| Hosting | Cloudflare Pages (`server-docs-public.pages.dev`) |
| Deploy Methods | Python script (`deploy_pages.py`), bash script (`deploy.sh`), wrangler (`wrangler_deploy.sh`) |

## Dependencies

- `mkdocs` — Static site generator
- `mkdocs-material` — Material Design theme

```bash
pip install mkdocs mkdocs-material
```

For deployment:
- `requests` (for Python deploy script)
- `wrangler` CLI (for wrangler deploy)

## Project Structure

```
server-docs-public/
├── mkdocs.yml              # MkDocs config — minimal nav (Home, Apps, Projects, Tech Stack)
├── deploy_pages.py         # Python script — Cloudflare Pages Direct Upload API
├── deploy.sh               # Bash script — Cloudflare Pages upload (token or email+key)
├── wrangler_deploy.sh      # Simple wrapper — wrangler deploy
├── docs/
│   ├── index.md            # Home page — hero section, Mermaid diagram, feature cards
│   ├── apps.md             # All 12 self-hosted apps described in cards
│   ├── projects.md         # 6 projects — BlockOps, Retro Arcade, Hermes, docs, backup, scraper
│   ├── tech-stack.md       # Full tech stack from OS to apps, with Mermaid diagram
│   ├── extra.css           # Custom styling (cards, grids, hero section, tags, etc.)
│   └── assets/
│       ├── server-icon.svg
│       └── favicon.svg
└── .gitignore
```

## Architecture / Data Flow

```
── Internet ──► Cloudflare DNS/CDN
                    │
            Cloudflare Tunnel (cloudflared)
                    │
               nginx reverse proxy
                    │
          ┌─────────┼──────────────┐
          │         │              │
     CasaOS     14 Docker     Game Servers
                 Containers   + AI Agent
                              + Cron Jobs
```

The public docs describe this architecture at a high level without specific port numbers, IPs, or config details.

## How to Run Locally

```bash
cd /home/kamalraj98/clones/server-docs-public

# Install dependencies
pip install mkdocs mkdocs-material

# Serve with live reload
mkdocs serve

# Build static site
mkdocs build

# Output to site/
```

## How to Deploy

Three deploy methods are available:

**Method 1 — wrangler (simplest):**
```bash
export CLOUDFLARE_API_TOKEN="your-token"
./wrangler_deploy.sh
```

**Method 2 — Python Direct Upload:**
```bash
export CLOUDFLARE_API_TOKEN="your-token"
python3 deploy_pages.py
```

**Method 3 — Bash script (token or email+key):**
```bash
export CLOUDFLARE_API_TOKEN="your-token"
./deploy.sh
```

## Agent Context

- **Owner:** Kamalraj
- **Git remote:** `git@github.com:kamalcr7/server-docs-public.git` (PUBLIC)
- **Site URL:** `https://server-docs-public.pages.dev`
- **This is the SANITIZED version** — no sensitive configs, ports, IPs, env files, or backup procedures
- **Compared to private `server-docs`:** Much simpler structure — only 4 nav pages vs 8 sections
- **Design:** Card-based UI with feature cards, project cards, info grids, and tech grids — all styled via `extra.css`
- **Deploy scripts:**
  - `deploy_pages.py` — Uses Python `requests` to upload via Cloudflare Direct Upload API
  - `deploy.sh` — Bash equivalent with same API approach
  - `wrangler_deploy.sh` — Simple shell wrapper calling `npx wrangler pages deploy`
- **Cloudflare account:** `bd9c942a32d790c221813a071ea2dc95`
- **Cloudflare project name:** `server-docs-public`
- **Auth options:** `CLOUDFLARE_API_TOKEN` (preferred) or `CF_EMAIL` + `CF_API_KEY`
- **Build output directory:** `site/` (after `mkdocs build`)
- **Nav structure:** Home → Apps → Projects → Tech Stack
- **Markdown extensions:** highlight, superfences (Mermaid), details, emoji, mark, tasklist, admonition, attr_list, tables, toc

---

*Generated for agent context — July 2026*
