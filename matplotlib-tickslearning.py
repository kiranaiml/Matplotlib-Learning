import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
sales = [120, 150, 140, 170, 180]

plt.figure(figsize=(8,5))

plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    label="Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.xticks(rotation=45, fontsize=12, color="red")
plt.yticks(fontsize=12, color="green")

plt.grid(True)
plt.legend()

plt.show()