import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 50, 55, 62, 68, 75, 82]
plt.scatter(hours,marks,color="red",marker="*",label="Study hours")
plt.title("Student study hours")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()