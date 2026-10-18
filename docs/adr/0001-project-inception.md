# 1. Project Inception and Initial Tech Stack

* Status: Accepted
* Date: 2026-10-18

## Context
Modul 3 membutuhkan deployment aplikasi web sederhana pada VPS Ubuntu 24.04 (`tiasrv`) dengan kriteria aman, ringan, dan mudah dikelola.

## Decision
Kami memutuskan untuk menggunakan stack berikut:
- **Framework:** Python Flask (ringan dan sesuai standar praktikum)
- **WSGI Server:** Gunicorn (diatur via systemd service `cc-m03.service`)
- **Reverse Proxy:** Caddy (menangani port 80 dan meneruskan ke Gunicorn port 8000)

## Consequences
- Aplikasi dapat berjalan otomatis di background secara andal.
- Siap untuk ditambahkan HTTPS/SSL dan domain kustom pada Modul 4.
