import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 140, 130, 160, 180]

plt.figure(figsize=(10,6))
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.plot(
    months,
    sales,
    linewidth=5,
    color="green",
    marker="*",
    markersize=7,
)

plt.show()