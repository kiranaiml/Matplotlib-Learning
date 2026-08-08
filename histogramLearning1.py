import matplotlib.pyplot as plt
heights = [150, 155, 160, 162, 158, 165, 170, 172, 168, 175,
           180, 177, 169, 163, 157, 161, 174, 171, 166, 159,
           153, 178, 182, 164, 167]
plt.hist(heights,bins=10,color="orange",edgecolor="Black")
plt.title("Distribution of Student Heights")
plt.xlabel("Height")
plt.ylabel("Number of Students")
plt.show()