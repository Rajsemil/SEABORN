import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
def graph():
	sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# Adding the subplot at the specified
# grid position
plt.subplot(121)
graph()
# Adding the subplot at the specified
# grid position
plt.subplot(122)
graph()
plt.show()