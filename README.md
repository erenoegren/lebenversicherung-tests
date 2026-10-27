# Lebensversicherung – Beitragsrechner mit automatisierten Tests

Ein kleines Python-Projekt zum Lernen von **Testautomatisierung mit pytest**.

## Was macht das Programm?

- Berechnet den **Monatsbeitrag** einer Risikolebensversicherung (abhängig von Alter, Versicherungssumme und Raucherstatus)
- Bildet zwei **Geschäftsvorfälle** ab: Beitragsfreistellung und Kündigung
- Prüft ungültige Eingaben (z. B. Alter unter 18) und gibt einen Fehler aus

## Tests

Die Datei `test_versicherung.py` enthält automatisierte Tests für:

- Normalfälle (richtiger Beitrag)
- Grenzwerte (Alter 18, 30, 31, 45, 46, 65)
- Fehlerfälle (ungültige Eingaben)
- Geschäftsvorfälle (Statuswechsel eines Vertrags)

## Starten

```bash
pip install pytest
python versicherung.py   # Beispiel ausführen
pytest -v                # Tests ausführen
```
