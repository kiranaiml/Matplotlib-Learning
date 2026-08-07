import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 35, 37, 36, 34]

plt.figure(figsize=(11,8))

plt.title("Weekly Temperature")
plt.xlabel("Days",fontsize=15,color="red")
plt.ylabel("Temperature", fontsize=16, color="blue")

plt.xticks(rotation=45, fontsize=11, color="red")

plt.plot(
    days,
    temperature,
    color="blue",
    linewidth=3,
    marker="o",
    markersize=14,
    label="Temperature"
)

plt.grid(True)
plt.xlim(1,6)
plt.ylim(31,37)

plt.legend()

plt.show()