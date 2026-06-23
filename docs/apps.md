# 📦 Apps

All the self-hosted apps running on my server. Every one is open source and runs in Docker.

<div class="feature-grid">

  <div class="feature-card">
    <span class="feature-card-icon">☁️</span>
    <h3>Nextcloud</h3>
    <p>My personal Dropbox — files, photos, contacts, calendar. PostgreSQL + Redis backend with auto-maintenance.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Cloud Storage</span><span class="tag">PostgreSQL</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🤖</span>
    <h3>Hermes Agent</h3>
    <p>Autonomous AI agent by Nous Research. Runs 24/7 — monitoring, reports, research, Telegram integration.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">AI</span><span class="tag">Automation</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔍</span>
    <h3>SearXNG</h3>
    <p>Private meta-search engine. Queries Google, DuckDuckGo, Wikipedia, etc. — no tracking, no logs, no profiling.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Search</span><span class="tag">Privacy</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📰</span>
    <h3>FreshRSS</h3>
    <p>RSS feed reader. Follows blogs, news sites, and creators. Works with FeedMe app on Android.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">RSS</span><span class="tag">Reader</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🏠</span>
    <h3>Homepage</h3>
    <p>Customizable dashboard that auto-discovers Docker containers and shows live status.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Dashboard</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📝</span>
    <h3>Obsidian</h3>
    <p>Note-taking vault in a container. Accessible from any browser, synced via Syncthing. Hermes writes to it too.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Notes</span><span class="tag">Syncthing</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔔</span>
    <h3>Ntfy</h3>
    <p>Push notification server. Simple HTTP API — every cron job and script can alert my phone.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Notifications</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔄</span>
    <h3>Syncthing</h3>
    <p>Decentralized P2P file sync. No cloud — devices sync directly. Keeps vault, photos, and docs in sync.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Sync</span><span class="tag">P2P</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📸</span>
    <h3>PiGallery2</h3>
    <p>Self-hosted photo gallery. Scans directories and generates thumbnails automatically.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Gallery</span><span class="tag">Photos</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🐳</span>
    <h3>Portainer</h3>
    <p>Docker management UI. View containers, logs, volumes, and networks without SSH.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Docker</span><span class="tag">Management</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📁</span>
    <h3>FileBrowser</h3>
    <p>Web-based file manager. Upload, download, preview files from any browser.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Files</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🎮</span>
    <h3>Epic Games Claimer</h3>
    <p>Auto-claims free Epic Games weekly. Runs on schedule, notifies when claimed.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">Automation</span><span class="tag">Gaming</span></div>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">💻</span>
    <h3>Hermes Workspace</h3>
    <p>Browser-based dev environment with editor and terminal. Code from any device.</p>
    <div class="tags" style="margin-top:0.5rem"><span class="tag">IDE</span><span class="tag">Web</span></div>
  </div>

</div>

---

## How they connect

```mermaid
flowchart LR
    subgraph Storage["💾 Storage Layer"]
        Nextcloud[Nextcloud]
        Postgres[PostgreSQL]
        Redis[Redis Cache]
    end
    
    subgraph Search["🔍 Search & Feed"]
        SearXNG[SearXNG]
        FreshRSS[FreshRSS]
    end
    
    subgraph Sync["🔄 Sync & Notify"]
        Syncthing[Syncthing]
        Ntfy[Ntfy]
        Obsidian[Obsidian]
    end
    
    subgraph Manage["⚙️ Management"]
        Portainer[Portainer]
        FileBrowser[FileBrowser]
        Homepage[Homepage]
    end
    
    subgraph AI["🤖 AI Layer"]
        Hermes[Hermes Agent]
        Workspace[Hermes Workspace]
    end
    
    Nextcloud --> Postgres
    Nextcloud --> Redis
    Syncthing --> Obsidian
    Hermes --> Ntfy
    Hermes --> Obsidian
```
