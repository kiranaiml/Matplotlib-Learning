import matplotlib.pyplot as plt
days=["Monday","Tuesday","Wednesday","Thurusday","Friday","Saturday"]
temperture=[45,3,44,33,32,12]
plt.title("Temperture at days")
plt.xlabel("Days")
plt.ylabel("Temperture")
plt.grid()
plt.plot(days,temperture)
plt.show()