import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

sales = [12000, 15000, 13500, 18000, 21000, 19500, 23000, 26000]
plt.figure(figsize=(10,6))
plt.xlabel("Month")
plt.ylabel("Monthly sales")
plt.title("2026 Sales")
plt.bar(months,sales,color="green",label="Sales")
plt.legend()
plt.xlim(1,6)
plt.ylim(0,30000)
plt.show()