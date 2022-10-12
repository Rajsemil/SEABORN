import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.swarmplot(x='species', y='sepal_width', data=data)
plt.show()