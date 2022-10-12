import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.countplot(x='species', data=data)
plt.show()