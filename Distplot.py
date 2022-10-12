import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.distplot(data['sepal_width'])
plt.show()