import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
tc = data.corr()
sns.heatmap(tc)
plt.show()