# Tests

Dieser Ordner enthält die definierten Testfälle zur Überprüfung der
Funktionalität des AI-Code-Bot Projekts.

Die Tests sind in drei Kategorien unterteilt:

- Unit Tests
- Integrationstests
- End-to-End Tests

---

## Anleitung

Um zu testen müssen folgende Vorbereitungen getroffen werden:
- README.md im Projektverzeichnis muss sorgfältig gelesen und verstanden worden sein
- API Key muss im Repository hinterlegt sein:
    > Repository > Settings > Secrets and variables > Actions > New Repository secret
    > Name des Secrets: DEEPSEEK_API_KEY
- Danach kann mit denen im tests-Ordner beigelegten Files, getestet werden

## Hinweise

- Die Tests wurden manuell durchgeführt.
- Die Ergebnisse wurden anhand der Konsolenausgaben sowie der
  generierten Dateien überprüft.
- Der Fokus lag auf der Stabilität, Fehlerbehandlung und der
  korrekten Integration aller Komponenten (CLI, Backend, API, CI/CD).