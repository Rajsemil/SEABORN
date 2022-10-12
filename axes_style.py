import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
def plot():
	sns.lineplot(x="sepal_length", y="sepal_width", data=data)
with sns.axes_style('darkgrid'):
	plt.subplot(211)
	plot()
plt.subplot(212)
plot()
plt.show()