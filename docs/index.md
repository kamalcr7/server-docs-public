<div class="hero-section">
  <h1>🚀 What I Run</h1>
  <p>This is my home server — an Ubuntu box running 14 containers, game servers, an AI agent, and everything in between. Built for fun, runs 24/7.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <span class="hero-stat-value">14</span>
      <span class="hero-stat-label">Containers</span>
    </div>
    <div class="hero-stat">
      <span class="hero-stat-value">99.9%</span>
      <span class="hero-stat-label">Uptime</span>
    </div>
    <div class="hero-stat">
      <span class="hero-stat-value">64 GB</span>
      <span class="hero-stat-label">RAM</span>
    </div>
    <div class="hero-stat">
      <span class="hero-stat-value">8+</span>
      <span class="hero-stat-label">Projects</span>
    </div>
  </div>
</div>

## How it all connects

```mermaid
flowchart LR
    Internet([🌐 Internet])
    
    subgraph Cloudflare [Cloudflare]
        CF[Proxy / CDN]
        Pages[Cloudflare Pages]
    end
    
    subgraph Server ["Home Server — Ubuntu 24.04"]
        Nginx[nginx<br/>Reverse Proxy]
        Containers[14 Docker<br/>Containers]
        Games[🎮 BlockOps<br/>🕹️ Arcade]
        Hermes[🤖 Hermes AI<br/>Agent]
    end
    
    Internet -->|DNS| CF
    CF -->|Tunnel| Nginx
    Nginx --> Containers
    Nginx --> Games
    Nginx --> Hermes
    Internet -->|This site| Pages
```

## What I use it for

<div class="feature-grid">

  <div class="feature-card">
    <span class="feature-card-icon">☁️</span>
    <h3>Cloud Storage</h3>
    <p>Nextcloud with 1.9 TB storage — my own Dropbox, no subscription needed.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔍</span>
    <h3>Private Search</h3>
    <p>SearXNG — aggregated search results with zero tracking or profiling.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🎮</span>
    <h3>Game Servers</h3>
    <p>Retro emulator arcade + browser-based FPS. Play with friends.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🤖</span>
    <h3>AI Agent</h3>
    <p>Hermes Agent — automates tasks, monitors the server, runs on a schedule.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📰</span>
    <h3>RSS Reader</h3>
    <p>FreshRSS — follows blogs and news feeds, always synced.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔄</span>
    <h3>File Sync</h3>
    <p>Syncthing keeps files in sync across all my devices without a cloud provider.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">📸</span>
    <h3>Photo Gallery</h3>
    <p>PiGallery2 — self-hosted photo gallery with albums and sharing.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🔔</span>
    <h3>Notifications</h3>
    <p>ntfy pushes alerts to my phone when something needs attention.</p>
  </div>

  <div class="feature-card">
    <span class="feature-card-icon">🗂️</span>
    <h3>File Browser</h3>
    <p>Web-based file manager for quick uploads and downloads.</p>
  </div>

</div>

---

## Explore

<div class="jump-links">
  <a href="apps/">📦 Apps</a>
  <a href="projects/">🚀 Projects</a>
  <a href="tech-stack/">🛠️ Tech Stack</a>
</div>
