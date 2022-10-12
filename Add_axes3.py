import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("iris")
def graph():
	sns.lineplot(x="sepal_length", y="sepal_width", data=data)
# adding the subplots
axes1 = plt.subplot2grid (
(7, 1), (0, 0), rowspan = 2, colspan = 1)
graph()
axes2 = plt.subplot2grid (
(7, 1), (2, 0), rowspan = 2, colspan = 1)
graph()
axes3 = plt.subplot2grid (
(7, 1), (4, 0), rowspan = 2, colspan = 1)
graph()
plt.show()