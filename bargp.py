import matplotlib.pyplot as plt


x = [i for i in range(10)]
y = [4, 1, 7, 2, 9, 2, 12, 5, 6, 8]
z = [4, 2, 9, 2, 4, 3, 1, 5, 5, 2]

x2 = [i+0.2 for i in range(10)]
# plt.bar(x,y)
plt.bar(x,y, color='red', width=0.2, label=2019)
plt.bar(x2,z, color='blue', width=0.2, label=2020)
plt.legend()
plt.show()
