# LB 324

## Aufgabe 2
Erklären Sie hier, wie man `pre-commit` installiert.

## Aufgabe 4
Erklären Sie hier, wie Sie das Passwort aus Ihrer lokalen `.env` auf Azure übertragen.



Beispiel-Anleitung (für README.md)
## Lokaler Start

### Voraussetzungen
- Python 3.11 (oder kompatibel)
- Git

### Setup
```bash
git clone <DEIN_REPO_LINK>
cd <REPO_ORDNER>

python -m venv .venv
# Windows PowerShell:
. .venv/Scripts/Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

ENV anlegen

Kopiere die Beispiel-ENV und passe sie an:

cp .env.example .env
# trage z.B. PASSWORD=meinpasswort ein

Starten
# Entwicklung:
flask --app app run --debug
# oder:
python app.py

# Produktion (lokal mit gunicorn):
gunicorn --bind=0.0.0.0:8000 app:app


Öffne: http://127.0.0.1:5000
 (oder http://127.0.0.1:8000
 bei gunicorn)


---

## 3) Tests (pytest) dokumentieren

In `README.md`:

```md
## Tests ausführen
```bash
pytest -q


Stelle sicher, dass `tests/test_app.py` **mindestens** einen Test enthält, der läuft.

---

## 4) Azure-Versuch nachvollziehbar dokumentieren

Da das Hosting nicht ging, schreibe offen in `README.md` (und ggf. `REPORT.md`), was du versucht hast:

- App Service Region: *Germany West Central*  
- App Service Plan: *Linux, F1 (Free)*  
- **App-Settings gesetzt**:
  - `SCM_DO_BUILD_DURING_DEPLOYMENT=true`
  - `ENABLE_ORYX_BUILD=true`
  - `ORYX_PYTHON_VERSION=3.11`
- GitHub Actions Workflow (`.github/workflows/deploy-main.yml`) eingerichtet.
- Fehler/Logs (aus dem Log Stream) mit kurzer Erklärung:
  - `ModuleNotFoundError: No module named 'dotenv'` (→ danach `python-dotenv` in `requirements.txt` ergänzt)
- **Screenshot(s)** vom Portal: Übersicht, Log Stream, ggf. Fehlermeldung „Application Error“.
- Link zum Deploy-Log / Workflow-Run (GitHub Actions).

> Ziel: Dein Lehrer sieht, **du hast die Cloud-Deploy-Kette verstanden und aufgebaut**, auch wenn Azure am Ende nicht mitspielt.

---

## 5) GitHub-Release & ZIP

Damit die Abgabe „eingefroren“ ist:

1. In GitHub: **Releases → Draft a new release**
2. Tag: `v1.0.0` (oder `submission-2025-09-22`)
3. **Release Notes:** kurzer Text + evtl. Link zu README.
4. **„Generate source code (zip)“** wird automatisch angehängt → das ist deine offizielle Abgabe.

> Alternativ: **Code → Download ZIP** (vom `main`-Branch) und in die Schulplattform hochladen **plus** Repo-Link mitgeben.

---

## 6) README-Vorlage (Copy/Paste)

```md
# Tagebuch-App (Flask)

## Kurzbeschreibung
Kleine Flask-App mit Tests und CI. Azure-Deployment versucht, lokal vollständig lauffähig.

## Projektstruktur
- `app.py` — Flask-App (Objekt `app`)
- `requirements.txt` — Python-Pakete
- `tests/` — pytest-Tests
- `templates/`, `static/` — (falls vorhanden)
- `.env.example` — Beispiel-Einstellungen (ohne Secrets)
- `.github/workflows/` — CI/CD (Tests & Deploy)

## Lokaler Start
```bash
python -m venv .venv
# Windows:
. .venv/Scripts/Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
flask --app app run --debug
# oder:
gunicorn --bind=0.0.0.0:8000 app:app

Tests
pytest -q

Azure-Deployment (Versuch)

App Service: Linux, Region: Germany West Central, Plan: F1 (Free)

App Settings:

SCM_DO_BUILD_DURING_DEPLOYMENT=true

ENABLE_ORYX_BUILD=true

ORYX_PYTHON_VERSION=3.11

Deploy via GitHub Actions (deploy-main.yml)

Problem/Logs:

ModuleNotFoundError: No module named 'dotenv' (behoben durch python-dotenv)

Trotz Fix reagierte Container nicht auf Port 8000 → „Application Error“

Screenshots: siehe docs/screenshots/ (falls angelegt)

startbefehel gunicorn --bind=0.0.0.0:8000 app:app

Bekannte Einschränkungen

Cloud-Deployment aktuell fehlerhaft, lokal läuft die App & Tests.
