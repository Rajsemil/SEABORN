import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.pairplot(data=data, hue='species')
plt.show()