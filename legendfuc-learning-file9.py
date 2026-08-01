import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 29, 35, 33]
plt.title("Weekly Temperture")
plt.xlabel("Days")
plt.ylabel("Temperture")
plt.grid(True)
plt.plot(
    days,
    temperature,
    color="green",
    marker="o",
    markersize=8,
    linewidth=5,

)
plt.show()