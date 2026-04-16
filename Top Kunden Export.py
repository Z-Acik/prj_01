import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cargo_data.csv', sep=';', encoding='utf-8-sig')

top_10 = df[df['Sendungstyp'] == 'Export']['Kunde'].value_counts().head(10)

ax = top_10.plot(kind='bar', color='#e67e22', figsize=(10, 7))
plt.title('Top 10 Export Kunden')

for i, v in enumerate(top_10):
    ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
