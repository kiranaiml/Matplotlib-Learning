import matplotlib.pyplot as plt
heights = [150, 155, 160, 162, 158, 165, 170, 172, 168, 175,
           180, 177, 169, 163, 157, 161, 174, 171, 166,
           159, 153, 178, 182, 164, 167]
plt.title("Height Distrubution")
plt.hist(heights,bins=5,color="green",edgecolor="black")
plt.xlabel("Heigth")
plt.ylabel("Frequency")
plt.show()