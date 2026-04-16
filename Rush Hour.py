import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cargo_data.csv', sep=';', encoding='utf-8-sig')

df = df[df['Sendungstyp'].isin(['Import', 'Export'])]

df['Stunde'] = df['Eingel_Zeit'].str.split(':').str[0].astype(int)

rush_hour = df.groupby(['Stunde', 'Sendungstyp']).size().unstack().fillna(0)

ax = rush_hour.plot(kind='bar', stacked=False, figsize=(14, 6), color=['#e67e22', '#3498db'], width=0.8)

plt.title('Daily Rush Hour: Vergleich Import vs. Export pro Stunde', fontsize=14)
plt.xlabel('Uhrzeit (Stunde)')
plt.ylabel('Anzahl Sendungen')
plt.xticks(rotation=0)
plt.legend(title='Sendungstyp')
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()
