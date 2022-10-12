import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('iris')
sns.lineplot(x='sepal_length', y='sepal_width', data=data)
plt.title('Set Context')
sns.set_context('paper')
plt.show()