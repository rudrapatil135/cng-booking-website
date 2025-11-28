# GitHub Copilot Instructions — cng-booking-website

This file gives concise, actionable guidance for AI code agents working in this repository.

**Project Snapshot**
- **Type:** Django web app (project folder `cng/`).
- **Apps:** `accounts`, `bookings`, `Gas` (each with `models.py`, `views.py`, `urls.py`, `migrations/`).
- **DB:** SQLite (`db.sqlite3`) used for local/dev. Migrations live under each app's `migrations/`.
- **Static & media:** `STATIC_ROOT` & Whitenoise configured in `cng/settings.py`; uploads go to `media/idproofs/` via model `FileField(upload_to='idproofs/')`.

**How to run locally**
- Create virtualenv and install: `python -m venv .venv` then `.
  .venv\Scripts\Activate.ps1` (PowerShell) and `pip install -r requirements.txt`.
- DB/migrations: `python manage.py migrate`.
- Dev server: `python manage.py runserver` (note: `DEBUG` is `False` by default in `cng/settings.py`; set the `DEBUG` env var or adjust locally for development).
- Tests: `python manage.py test`.

**Production notes**
- `cng/settings.py` expects `SECRET_KEY` from the environment and uses `whitenoise.storage.CompressedManifestStaticFilesStorage`.
- Run `python manage.py collectstatic` before deploying static assets.
- `ALLOWED_HOSTS` includes `cng-booking-website.onrender.com` — update for other hosts.

**Key code patterns and examples**
- File uploads: forms that accept uploaded id proofs use `request.FILES`. See `bookings/views.py` -> `connection_request` which constructs the form with `request.FILES` and the model `ConnectionRequest` defines `idproof = models.FileField(upload_to='idproofs/')`.
- Auth: many views use `@login_required` (imported from `django.contrib.auth.decorators`). Follow this pattern for views that require an authenticated user.
- Payment/session gating: the payment flow sets `request.session['payment_completed'] = True` in `bookings/views.py`; downstream pages check this session key to allow booking (`book_cng` view).
- Models with choices: `ConnectionRequest.status` and `Payment.status` use choice tuples. Refer to `bookings/models.py` for exact choice strings (`'Pending'`, `'Approved'`, `'Rejected'`, `'Success'`, `'Failed'`).

**Where to edit / add features**
- Add new view: `app/views.py` -> expose via app `urls.py` -> include in project `cng/urls.py`.
- Templates live under top-level `templates/` with subfolders like `booking/`, `payment/`, `home/`. Use `templates/base.html` for layout changes.
- Static assets: place under `static/` (project root) and run `collectstatic` for production builds.

**Integration & security notes (discoverable in code)**
- Payment data: `bookings.models.PaymentDetail` stores card fields directly (OneToOne to `User`). This is present in the codebase (likely for demo/testing). Do not add real card data in tests or fixtures.
- Whitenoise is used (`whitenoise.middleware.WhiteNoiseMiddleware`), so static serving is handled by the app in production builds.

**Quick references (files to open first)**
- `cng/settings.py` — global configuration (DEBUG, STATIC, ALLOWED_HOSTS, SECRET_KEY fallback).
- `manage.py` — entrypoint for migrations, server, and tests.
- `bookings/models.py`, `bookings/views.py`, `bookings/forms.py` — booking, payment and idproof handling.
- `templates/booking/` and `templates/payment/` — user-facing flows.

If anything is missing or you want examples added (e.g., preferred linting, CI commands, or environment variable names), please tell me which area to expand.
