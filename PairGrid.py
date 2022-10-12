import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('iris')
plot = sns.PairGrid(data)
plot.map(plt.plot)
plt.show()