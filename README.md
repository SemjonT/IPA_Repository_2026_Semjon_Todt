# AI Code Optimization

Dieses Projekt automatisiert die Analyse und Optimierung von Python-Code.  
Es besteht aus zwei separaten Komponenten:

1. **Backend** – verarbeitet Code, führt Linting durch und kommuniziert mit der DeepSeek API.  
2. **CLI-Client** – Schnittstelle für den Entwickler oder GitHub Actions, um Code an das Backend zu senden.

> **Wichtig:** Das Backend muss **immer zuerst gestartet** werden, bevor der CLI-Client verwendet werden kann.

---

## Voraussetzungen

- Python 3.10+
- Git
- Zugriff auf die DeepSeek API und gültiger API-Key
- Lokale Entwicklungsumgebung mit installierten Abhängigkeiten
    > pip install -r requirements.txt

---

## Backend starten

1. **.env Datei erstellen**  
   Erstelle im Projektverzeichnis eine `.env`-Datei mit folgendem Inhalt:
   ```env
   DEEPSEEK_API_KEY=<DEIN_API_KEY_HIER>

   Falls ein Server besteht kann die Backend URL festgesetzt werden:
   ```env
   BACKEND_URL=<DEINE_BACKEND_URL>

2. **Backend mit folgendem Command starten**
    python3 -m uvicorn backend.main:app --reload

## CLI starten

**Command**
python3 cli/cli_client.py <datei>

**Beispiel**
> python3 cli/cli_client.py tests/U01.py

## Workflow
1. **Setup**
    Branchname ändern (hier *test*)
    ```yml
    on:
        push:
            branches:
            - test
        pull_request:

2. **Pull/Push Request auf gewählten Branch ausführen**

3. **Auf GitHub Actions gehen und optimized-code von Artefakten herunterladen**