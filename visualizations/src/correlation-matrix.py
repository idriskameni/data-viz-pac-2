import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/correlation-matrix.data')
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

corr = df.iloc[:, :4].corr()

fig, ax = plt.subplots()

sns.heatmap(corr, annot=True, cmap='coolwarm', square=True, 
            xticklabels=corr.columns.values, yticklabels=corr.columns.values,
            annot_kws={'fontsize':12},
            ax=ax
)

ax.set_title('Correlation Matrix del joc de dades \'Iris\'')

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(rotation=0)

ax.text(0.5, -0.25, 'Font:UCI Machine Learning Repository [http://archive.ics.uci.edu/ml].\nIrvine, CA: University of California, School of Information and Computer Science.', ha='center', va='bottom', transform=plt.gca().transAxes)

fig.set_size_inches(8, 4)
plt.savefig('../images/correlation-matrix.jpg', dpi=300, bbox_inches='tight')