import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/correlation-matrix.csv', delimiter=';')

corr_matrix = df.corr()

print(corr_matrix)

fig, ax = plt.subplots()

im = ax.imshow(corr_matrix, cmap='coolwarm')
ax.figure.colorbar(im, ax=ax)

ax.set_title('Habitants de Ripollet per any')
ax.set_xlabel('Any')
ax.set_ylabel('Habitants')

ax.set_title("Correlation Matrix")

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

fig.set_size_inches(8, 4)
plt.savefig('../images/correlation-matrix.jpg', dpi=300, bbox_inches='tight')