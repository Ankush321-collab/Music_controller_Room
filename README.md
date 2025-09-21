# Music-Controller-Web-App-Tutorial

**The code for Tech With Tim's "Django & React Full Stack Web App Tutorial" series.**

---

## Project Overview

This repository contains the source code for the **Music Controller** full-stack tutorial (Django backend + React frontend) from Tech With Tim. The app demonstrates how to build a full-stack web application that allows users to control music playback, manage rooms, and interact via a REST API powered by Django REST Framework (DRF) with a React frontend.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)

  * [Backend (Django)](#backend-django)
  * [Frontend (React)](#frontend-react)
* [Environment Variables](#environment-variables)
* [Run (Development)](#run-development)
* [Build (Production)](#build-production)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)
* [About / Promotion](#about--promotion)

---

## Features

* Django REST Framework API for rooms, users, and music control endpoints
* Token-based (or session) authentication examples
* React frontend showing real-time room states and simple player controls
* Example of unique code generation for rooms

---

## Prerequisites

* Python 3.8+ (3.10 recommended)
* Node.js 16+ / npm 8+
* pip (for Python dependencies)
* (Optional) virtualenv or venv for isolating Python packages

---

## Setup Instructions

> Follow the steps below to get the project running locally. The repo is split into tutorial folders; each tutorial (e.g. "Tutorial 1") contains a working snapshot.

### 1) Install Required Python Modules

```bash
# from the repo root (or inside a specific tutorial folder if present)
pip install -r requirements.txt
```

### 2) Backend (Django)

1. `cd` into the desired tutorial folder if the repository contains multiple tutorial directories. For example:

```bash
cd "Tutorial x"
```

2. Make migrations and migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. (Optional) Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

The backend API will typically be available at `http://127.0.0.1:8000/`.

---

### 3) Frontend (React)

1. `cd` into the frontend folder:

```bash
cd frontend
```

2. Install Node dependencies:

```bash
npm install
# or
npm i
```

3. Start the frontend in development mode (hot reloading):

```bash
npm run dev
# or sometimes
npm start
```

4. For a production build:

```bash
npm run build
```

If the frontend is served separately, it typically runs on `http://localhost:3000` or the port configured in the `package.json`.

---

## Environment Variables

If the project uses an `.env` file or `settings.py` expects environment values, create a `.env` in the backend folder (or update `settings.py`) with keys similar to:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
# DB settings if you use Postgres / custom DB
# FRONTEND_URL=http://localhost:3000
```

Adjust names to match the repo's expectations.

---

## Run (Development)

1. Start Django backend: `python manage.py runserver`
2. Start React frontend (from `frontend`): `npm run dev`
3. Open the frontend URL (commonly `http://localhost:3000`) and it should communicate with the Django API at `http://127.0.0.1:8000`.

---

## Build (Production)

1. Build frontend: from `frontend` run `npm run build`.
2. Serve the static `build` folder via a web server (Netlify, Vercel, or serve from Django using `django.contrib.staticfiles` or a reverse proxy).
3. Ensure CORS and static file settings in `settings.py` are configured for production.

---

## Troubleshooting

* **`ModuleNotFoundError` / missing packages**: Ensure virtualenv is active and `pip install -r requirements.txt` succeeded.
* **Frontend not contacting backend**: Check CORS settings and the `FRONTEND_URL` / API base URL used in the React app (often in an `.env` or `src/config` file).
* **Port conflicts**: Ensure no other process is using ports 3000 or 8000.
* **`Room.objects.filter(code=code).count` bug**: Use `count()` (method) or `exists()` for a faster check: `if not Room.objects.filter(code=code).exists():`.

---

## Contributing

Contributions welcome! Please open an issue or a pull request with a clear description of changes. Keep code style consistent with the project; add tests where practical.

---

## License

This repository is provided for educational purposes. Unless otherwise specified in a `LICENSE` file, you can add `MIT` or the license of your choice. Add a `LICENSE` file at the repo root if you intend to open-source it.

---

## About / Promotion

💻 Launch Your Software Development Career Today!

No degree? No problem! This tutorial and related courses show hands-on full-stack projects that help you build a portfolio and prepare for entry-level roles.

* **Why Join?**

  * \$70k+ starting salary potential
  * Self-paced learning
  * Affordable compared to expensive bootcamps
  * Real projects to build your portfolio

👉 Start your journey today—practice, build projects, and apply.

---

*If you want I can also:*

* Create a `CONTRIBUTING.md` or `LICENSE` file.
* Generate a cleaned `requirements.txt` or a `Procfile` for deployment.
* Tailor the README to a specific tutorial folder (e.g., "Tutorial 3 - Room API").
