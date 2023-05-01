import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.read_csv('../data/ohlc-chart.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df.index)

df_april = df.loc['2023-04']

print(df_april)
fig, ax = plt.subplots()

mpf.plot(df_april, type='candle', style='charles', ax=ax)

ax.set_title('OHLC Chart')
ax.set_ylabel('Price')

fig.set_size_inches(8, 4)
plt.savefig('../images/ohlc-chart.jpg', dpi=300, bbox_inches='tight')

