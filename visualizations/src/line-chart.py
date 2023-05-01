import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/line-chart.csv')

df = df.loc[df['NOM_ENS'] == 'Ajuntament de Ripollet']
df = df.drop(['CODI_10', 'NOM_ENS', 'HOMES', 'DONES'], axis=1)
df = df.sort_values('ANY')

fig, ax = plt.subplots()

ax.plot(df['ANY'], df['TOTAL'])

ax.set_title('Habitants de Ripollet per any')
ax.set_xlabel('Any')
ax.set_ylabel('Habitants')

ax.text(0.5, -0.25, 'Font: Dades històriques de població \ndels municipis de Catalunya (Dades obertes Catalunya)', ha='center', va='bottom', transform=plt.gca().transAxes)

plt.savefig('../../line-chart.jpg', dpi=300, bbox_inches='tight')