#!/usr/bin/env python3
"""Upload MkDocs site to Cloudflare Pages via Direct Upload API using requests.
Requires env vars: CLOUDFLARE_API_TOKEN, or CF_EMAIL + CF_API_KEY.
"""
import hashlib, json, os, sys, mimetypes

SITE_DIR = "/home/kamalraj98/workspace/server-docs-public-repo/site"
ACCOUNT = "bd9c942a32d790c221813a071ea2dc95"
PROJECT = "server-docs-public"

# Auth: prefer token, fall back to email+key
api_token = os.environ.get("CLOUDFLARE_API_TOKEN")
email = os.environ.get("CF_EMAIL", "kamalraj05@gmail.com")
api_key = os.environ.get("CF_API_KEY")

if not (api_token or api_key):
    print("ERROR: Set CLOUDFLARE_API_TOKEN or CF_API_KEY + CF_EMAIL", file=sys.stderr)
    sys.exit(1)

import requests

# Build manifest
manifest = {}
files = []
for root, dirs, fnames in os.walk(SITE_DIR):
    for fname in fnames:
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, SITE_DIR)
        with open(path, "rb") as f:
            content = f.read()
        manifest[rel] = hashlib.sha256(content).hexdigest()
        files.append((rel, path, content))

print(f"Files: {len(files)}, Size: {sum(len(c) for _, _, c in files)}", file=sys.stderr)

# Build multipart
files_data = [("manifest", (None, json.dumps(manifest), "application/json"))]
for rel, path, content in files:
    mime = mimetypes.guess_type(rel)[0] or "application/octet-stream"
    files_data.append((rel, (rel, content, mime)))

# Upload
url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/pages/projects/{PROJECT}/deployments"
headers = {}
if api_token:
    headers["Authorization"] = f"Bearer {api_token}"
else:
    headers["X-Auth-Email"] = email
    headers["X-Auth-Key"] = api_key

print(f"Uploading to {url}...", file=sys.stderr)
resp = requests.post(url, headers=headers, files=files_data, timeout=180)
data = resp.json()

print(f"Success: {data.get('success')}")
r = data.get("result", {})
print(f"URL: {r.get('url', '?')}")
print(f"Env: {r.get('environment', '?')}")
print(f"Aliases: {r.get('aliases', [])}")
print(f"Deploy ID: {r.get('id', '?')}")

if not data.get('success'):
    print(f"Errors: {data.get('errors', [])}")
