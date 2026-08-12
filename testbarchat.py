import matplotlib.pyplot as plt
subjects = ["Python", "Pandas", "NumPy", "Matplotlib", "SQL"]
marks = [85, 78, 90, 82, 75]
plt.figure(figsize=(10,7))
plt.bar(subjects,marks,color="red",edgecolor="black",label="Marks at subject")
plt.title("Student progress")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()
plt.show()