import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
sns.rugplot(data=data)
plt.show()