import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.read_csv('../data/ohlc-chart.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df.index)

df_april = df.loc['2023-04']

fig, ax = plt.subplots()

mpf.plot(df_april, type='candle', style='charles', ax=ax)

ax.set_title('OHLC Chart del preus de les accions d\'Amazon l\'Abril del 2023')
ax.set_ylabel('Dates')
ax.set_ylabel('Preu')

ax.text(0.5, -0.25, 'Font: Yahoo Finance - \nAmazon.com, Inc. (AMZN)', ha='center', va='bottom', transform=plt.gca().transAxes)

fig.set_size_inches(8, 4)
plt.savefig('../images/ohlc-chart.jpg', dpi=300, bbox_inches='tight')

