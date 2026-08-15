import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [15000, 18000, 16500, 22000, 25000, 28000]

expenses = [9000, 10000, 9500, 12000, 13500, 15000]
plt.subplot(1,2,1)
plt.plot(months, sales, color="green", marker="o")

plt.subplot(1,2,2)
plt.bar(months, expenses, color="red")

plt.savefig("sample_data.png", dpi=300, bbox_inches="tight")
plt.show()