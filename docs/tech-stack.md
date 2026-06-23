# 🛠️ Tech Stack

What makes this server tick — from the OS right up to the application layer.

```mermaid
flowchart TD
    subgraph Apps["📱 Applications"]
        Nextcloud[Nextcloud]
        SearXNG[SearXNG]
        FreshRSS[FreshRSS]
        Syncthing[Syncthing]
        Ntfy[Ntfy]
        Obsidian[Obsidian]
        PiGallery[PiGallery2]
        Portainer[Portainer]
    end
    
    subgraph Runtime["⚙️ Runtime & Orchestration"]
        Docker[Docker + containerd]
        CasaOS[CasaOS]
        Nginx[nginx]
        Node[Node.js]
        Python[Python 3.x]
    end
    
    subgraph Infra["☁️ Infrastructure & Networking"]
        Cloudflare[Cloudflare<br/>DNS / Tunnel / CDN]
        Cloudflared[cloudflared<br/>Tunnel Agent]
        systemd[systemd<br/>Service Manager]
    end
    
    subgraph OS["💿 Operating System"]
        Ubuntu[Ubuntu 24.04 LTS]
        ZFS[ZFS Filesystem]
        Networking[NetworkManager]
    end
    
    Apps --> Docker
    Docker --> OS
    Docker --> Nginx
    Docker --> Node
    Nginx --> Cloudflared
    Cloudflared --> Cloudflare
    CasaOS --> Docker
    systemd --> Node
    systemd --> Python
    systemd --> Cloudflared
    
    style OS fill:#e95420,color:#fff
    style Infra fill:#6366f1,color:#fff
    style Runtime fill:#22d3ee,color:#111
    style Apps fill:#a78bfa,color:#fff
```

## Operating System & Hardware

<div class="info-grid">

  <div class="info-card">
    <div class="info-card-label">OS</div>
    <div class="info-card-value">Ubuntu 24.04 LTS</div>
  </div>
  <div class="info-card">
    <div class="info-card-label">CPU</div>
    <div class="info-card-value">AMD Ryzen 5 5600G</div>
  </div>
  <div class="info-card">
    <div class="info-card-label">RAM</div>
    <div class="info-card-value">64 GB DDR4</div>
  </div>
  <div class="info-card">
    <div class="info-card-label">GPU</div>
    <div class="info-card-value">RTX 4060 Ti</div>
  </div>

</div>

## Runtime & Cloud

<div class="tech-grid">

  <div class="tech-item">
    <span>🐳</span>
    <span>Docker</span>
  </div>
  <div class="tech-item">
    <span>🪟</span>
    <span>CasaOS</span>
  </div>
  <div class="tech-item">
    <span>🔀</span>
    <span>nginx</span>
  </div>
  <div class="tech-item">
    <span>💚</span>
    <span>Node.js</span>
  </div>
  <div class="tech-item">
    <span>🐍</span>
    <span>Python</span>
  </div>
  <div class="tech-item">
    <span>🔶</span>
    <span>Cloudflare</span>
  </div>
  <div class="tech-item">
    <span>🔗</span>
    <span>cloudflared</span>
  </div>
  <div class="tech-item">
    <span>⚡</span>
    <span>Hermes Agent</span>
  </div>
  <div class="tech-item">
    <span>📦</span>
    <span>systemd</span>
  </div>
  <div class="tech-item">
    <span>🗄️</span>
    <span>PostgreSQL</span>
  </div>
  <div class="tech-item">
    <span>🔥</span>
    <span>Redis</span>
  </div>
  <div class="tech-item">
    <span>🔌</span>
    <span>Socket.io</span>
  </div>
  <div class="tech-item">
    <span>🌐</span>
    <span>EmulatorJS</span>
  </div>
  <div class="tech-item">
    <span>📊</span>
    <span>MkDocs Material</span>
  </div>

</div>

---

### Key Principles

- ✅ **Open source first** — Every app is free and open source software
- 🔒 **Self-hosted** — No third-party cloud dependencies for core services
- ⚡ **Automation** — Cron jobs handle backups, updates, monitoring
- 🔄 **Redundancy** — Docker volumes backed up daily, Syncthing mirrors critical data
- 🛡️ **Cloudflare** — DNS, CDN, DDoS protection, and tunnel for secure access
