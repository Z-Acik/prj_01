import pandas as pd

df = pd.read_csv('cargo_data.csv', sep=';', encoding='utf-8-sig')

df['Tonnage'] = df['Gewicht'] / 1000

tonnage_stats = df.groupby(['Sendungstyp', 'Kunde'])['Tonnage'].sum().sort_values(ascending=False)

print("\n--- TONNAGE EXPORT ---")
print(tonnage_stats['Export'].map('{:.2f} t'.format))

print("\n--- TONNAGE IMPORT ---")
print(tonnage_stats['Import'].map('{:.2f} t'.format))
