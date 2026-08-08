import matplotlib.pyplot as plt
sales = [120, 150, 130, 180, 200, 170, 220, 250, 230, 280]
plt.hist(sales,bins=6,color="Blue",edgecolor="black")
plt.title("Sales at Market")
plt.xlabel(" Sales ")
plt.ylabel(" High Sale")
plt.show()