#!/bin/bash
# Upload server docs to Cloudflare Pages
# Requires: CLOUDFLARE_API_TOKEN or CF_EMAIL + CF_API_KEY
set -e

SITE_DIR="/home/kamalraj98/workspace/server-docs-public-repo/site"

# Use token if available, otherwise email+key
if [ -n "$CLOUDFLARE_API_TOKEN" ]; then
  npx wrangler@latest pages deploy "$SITE_DIR" --project-name=server-docs-public 2>&1
else
  echo "Using email+key auth..."
  EMAIL="${CF_EMAIL:-kamalraj05@gmail.com}"
  API_KEY="${CF_API_KEY}"
  ACCOUNT="bd9c942a32d790c221813a071ea2dc95"
  PROJECT="server-docs-public"

  if [ -z "$API_KEY" ]; then
    echo "ERROR: Set CLOUDFLARE_API_TOKEN or CF_API_KEY"
    exit 1
  fi

  # Build manifest as JSON
  python3 -c "
import json, hashlib, os
manifest = {}
for root, dirs, fnames in os.walk('$SITE_DIR'):
    for f in fnames:
        path = os.path.join(root, f)
        rel = os.path.relpath(path, '$SITE_DIR')
        with open(path, 'rb') as fh:
            manifest[rel] = hashlib.sha256(fh.read()).hexdigest()
print(json.dumps(manifest))
" > /tmp/cf_manifest.json

  MANIFEST=$(cat /tmp/cf_manifest.json)
  CMD="curl -s -X POST 'https://api.cloudflare.com/client/v4/accounts/${ACCOUNT}/pages/projects/${PROJECT}/deployments' \
    -H 'X-Auth-Email: ${EMAIL}' \
    -H 'X-Auth-Key: ${API_KEY}' \
    -F 'manifest=${MANIFEST}'"

  find "$SITE_DIR" -type f | sort | while read f; do
      rel=$(echo "$f" | sed "s|${SITE_DIR}/||")
      CMD="$CMD -F '${rel}=@${f}'"
  done

  CMD="$CMD 2>/dev/null"
  eval "$CMD"
fi
