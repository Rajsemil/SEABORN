import seaborn as sns  
import matplotlib.pyplot as plt  
data = sns.load_dataset("iris")  
plt.figure(figsize = (int(input("Enter a width number: ")), int(input("Enter a height number: ")))) 
sns.lineplot(x="sepal_length", y="sepal_width", data=data)  
sns.despine() 
plt.show()