#!/bin/bash
# Deploy site to Cloudflare Pages via wrangler
# Requires: CLOUDFLARE_API_TOKEN exported in env
set -e
cd /home/kamalraj98/workspace/server-docs-public-repo
npx wrangler@latest pages deploy site/ --project-name=server-docs-public 2>&1
