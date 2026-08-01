import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]

income = [25000, 28000, 30000, 35000, 40000]

expense = [18000, 20000, 22000, 24000, 26000]
plt.title("Monthly income and expense")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.grid(True)
plt.plot(
    months,
    income,
    color="green",
    linestyle="--",
    markersize=9,
    linewidth=3,
    label="Income",
    marker="o"

)
plt.plot(
    months,
    expense,
    color="red",
    linestyle="--",
    marker="o",
    label="Expense",
    markersize=9,
    linewidth=5
)
plt.legend()
plt.show()