import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.barplot(x='species', y='sepal_length', data=data)
plt.show()