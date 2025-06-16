import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV-Datei laden
df = pd.read_csv("C:\\Users\\KASIMOO\\OneDrive - Daimler Truck\\Dokumente\\ETL-Projekt Sensordaten\\data\\sensordaten_onur.csv", parse_dates=["timestamp"])

# Fehlende Werte anzeigen
print("Fehlende Werte vor Bereinigung:")
print(df.isnull().sum())

# Fehlende Werte bereinigen (z. B. mit Mittelwert füllen)
df["temperature_C"].fillna(df["temperature_C"].mean(), inplace=True)
df["humidity_%"].fillna(method="ffill", inplace=True)

# Statistische Kennzahlen
print("\n--- Statistik ---")
print(f"Temperatur Ø: {df['temperature_C'].mean():.2f} °C")
print(f"Luftfeuchtigkeit Ø: {df['humidity_%'].mean():.2f} %")

# Visualisierung
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["temperature_C"], label="Temperatur (°C)")
plt.plot(df["timestamp"], df["humidity_%"], label="Luftfeuchtigkeit (%)")
plt.xlabel("Zeit")
plt.ylabel("Wert")
plt.title("Sensordatenverlauf")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()