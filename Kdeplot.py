import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.kdeplot(x='sepal_length', y='sepal_width', data=data)
plt.show()