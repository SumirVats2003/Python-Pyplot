import matplotlib.pyplot as plt
x = [1,4,7,9]
y = [2,45,12,48]

plt.plot(x,y)
# plt.plot(x,y, 'r')
# plt.plot(x,y, 'r-.')
# plt.plot(x,y, 'r--')
plt.title("Height vs Time")
plt.xlabel('Time')
plt.ylabel('Height')
plt.show()
