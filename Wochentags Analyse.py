import pandas as pd
import matplotlib.pyplot as plt

# 1. Daten laden
df = pd.read_csv('cargo_data.csv', sep=';', encoding='utf-8-sig')

# 2. Filter: Nur Import und Export (ohne Dienstleistung)
df = df[df['Sendungstyp'].isin(['Import', 'Export'])]

# 3. Wochentag extrahieren
df['Eingel_Dat'] = pd.to_datetime(df['Eingel_Dat'], format='%d.%m.%Y')
df['Wochentag'] = df['Eingel_Dat'].dt.day_name()

# 4. Sortierung festlegen (Montag bis Sonntag)
tage_ordnung = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['Wochentag'] = pd.Categorical(df['Wochentag'], categories=tage_ordnung, ordered=True)

# 5. Gruppieren nach Wochentag und Typ (Anzahl Sendungen)
wochentag_stats = df.groupby(['Wochentag', 'Sendungstyp']).size().unstack().fillna(0)

# 6. Visualisierung als gruppierte Balken
ax = wochentag_stats.plot(kind='bar', stacked=False, figsize=(12, 6), color=['#e67e22', '#3498db'], width=0.8)

plt.title('Wochentags-Analyse: Import vs. Export (Anzahl Sendungen)', fontsize=14)
plt.ylabel('Anzahl Sendungen')
plt.xlabel('Wochentag')
plt.xticks(rotation=45)
plt.legend(title='Sendungstyp')
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
