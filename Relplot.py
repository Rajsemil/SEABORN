import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
# creating the relplot
sns.relplot(x='sepal_width', y='species', data=data)
plt.show()