# 1. Project Inception and Initial Tech Stack

* Status: Accepted
* Date: 2026-10-18

## Context
Modul 3 membutuhkan deployment aplikasi web sederhana pada VPS Ubuntu 24.04 (`tiasrv`).

## Decision
Kami menggunakan stack berikut:
- **Framework:** Python Flask
- **WSGI Server:** Gunicorn (diatur via systemd service `cc-m03.service`)
- **Reverse Proxy:** Caddy (port 80 meneruskan ke Gunicorn port 8000)

## Consequences
- Aplikasi berjalan otomatis di background secara andal.
- Siap untuk integrasi domain/HTTPS pada Modul 4.
