import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

temperature = [28, 30, 33, 36, 38, 35]
plt.figure(figsize=(11,8))
plt.grid()
plt.title("Monthly Temperture ")
plt.xlabel("Months")
plt.ylabel("Temperture")

plt.plot(
    months,
    temperature,
    color="red",
    linestyle="--",
    linewidth=4,
    marker="*",
    markersize=15,
    label="Temperture"
)
plt.legend()
plt.grid()
plt.show()