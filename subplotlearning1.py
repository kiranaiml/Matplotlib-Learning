import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

temperature = [28, 30, 29, 31, 32, 30, 27]

humidity = [65, 60, 68, 55, 52, 58, 72]

rainfall = [2, 0, 5, 1, 0, 8, 12]

wind_speed = [10, 12, 8, 15, 18, 14, 9]
plt.figure(figsize=(10,6))
plt.subplot(1,4,1)
plt.title("Temperture chart")
plt.plot(days,temperature)
plt.subplot(1,4,2)
plt.title("Humudity chart")
plt.bar(days,humidity)
plt.subplot(1,4,3)
plt.title("Rainfall chart")
plt.plot(days,rainfall)
plt.subplot(1,4,4)
plt.title("Wind speed chart")
plt.bar(days,wind_speed)
plt.tight_layout()
plt.show()