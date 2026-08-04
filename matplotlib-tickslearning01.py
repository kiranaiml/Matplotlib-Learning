import matplotlib.pyplot as plt
months = ["January", "February", "March", "April", "May", "June"]

sales = [120, 140, 135, 160, 180, 200]

plt.figure(figsize=(10,6))
plt.title("Monthly wise Sales")
plt.xlabel("Months")
plt.ylabel("Sale")
plt.plot(
    months,
    sales,
    color="Green",
    linestyle="--",
    linewidth=3,
    marker="*",
    markersize=13,
    label="Sales"
)

plt.xticks(color="green", fontsize=11, rotation=30)
plt.yticks(fontsize=13, color="blue")
plt.grid(True)
plt.legend()
plt.show()