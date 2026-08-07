import matplotlib.pyplot as plt
categories = ["Food", "Rent", "Transport", "Education", "Shopping", "Savings"]

amount = [8000, 12000, 3500, 5000, 2500, 9000]
plt.pie(amount,labels=categories,autopct="%1.1f%%",colors=["yellow","red","purple","green","blue","brown"])
plt.show()