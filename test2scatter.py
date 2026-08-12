import matplotlib.pyplot as plt
age = [18, 19, 20, 21, 22, 23, 24]
salary = [15000, 18000, 22000, 25000, 30000, 35000, 42000]
plt.scatter(age,salary,color="blue",edgecolors="black",marker=">",label="Age wise salary")
plt.title('Age vs Salary')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()