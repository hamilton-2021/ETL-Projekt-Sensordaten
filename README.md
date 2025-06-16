# Sensordaten ETL-Pipeline (Beispielprojekt)

Dieses Projekt simuliert eine einfache ETL-Pipeline zur Verarbeitung von Sensordaten (Temperatur und Luftfeuchtigkeit), wie sie z. B. in einem vernetzten Bus mit CTP-ECU erfasst werden könnten.

## Schritte:
- Datenquelle: CSV-Datei mit Zeitstempel, Temperatur und Luftfeuchtigkeit
- Bereinigung: Entfernen fehlender Werte
- Analyse: Durchschnitt, Standardabweichung, Visualisierung
- Vorbereitung auf Speicherung (Azure Blob optional)

## Tools:
- Python (Pandas, NumPy)
- Google Colab / Jupyter Notebook (lokal oder in Azure Databricks)