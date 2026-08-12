import matplotlib.pyplot as plt
categories = ["Food", "Rent", "Transport", "Education", "Shopping"]
amount = [8000, 12000, 3500, 5000, 2500]
plt.pie(amount,labels=categories,autopct="%1.1f%%",colors=["red","pink","green","blue","purple"])
plt.show()