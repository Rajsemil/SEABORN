import matplotlib.pyplot as plt
import seaborn as sns
flights=sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
sns.clustermap(flights,linewidths=.5,cmap="coolwarm",col_cluster=False)
plt.show()