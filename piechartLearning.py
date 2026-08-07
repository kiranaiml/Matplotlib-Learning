import matplotlib.pyplot as plt
companies = ["Google", "Microsoft", "Amazon", "Apple", "Meta", "Nvidia"]

revenue = [320, 280, 240, 210, 180, 350]
plt.pie(revenue,labels=companies,autopct="%1.1f%%",colors=["blue","green","grey","red","darkblue","lightgreen"])
plt.show()