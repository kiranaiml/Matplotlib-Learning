import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

expenses = [8500, 9200, 7800, 10500, 11200, 9800, 12500, 11800]
plt.title("Monthly Expensation")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.bar(months,expenses,color="blue",label="Expense")
plt.legend()
plt.xlim(0,8)
plt.show()