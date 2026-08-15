import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12000, 15000, 13500, 18000, 21000, 24000]
expenses = [7000, 8500, 8000, 9500, 11000, 12500]
plt.subplot(1,2,1)
plt.title("Revenue chart")
plt.plot(months,revenue)
plt.subplot(1,2,2)
plt.bar(months,expenses)
plt.title("Expense chart")
plt.show()