# subar_apex
SubarApex

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
