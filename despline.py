import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('iris')
sns.limeplot(x='sepal_length', y='sepal_width', data=data)
sns.depine()
plt.show()