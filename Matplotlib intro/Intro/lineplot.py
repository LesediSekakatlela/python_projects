import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [2,4,6,8,7,6,5,4]#values can move up and down

plt.plot(x, y, 'g-.o')
plt.axis([0,10,0,10])
plt.xlabel("Horizontal Title")
plt.ylabel("Vertical Title")
plt.title("Your Title")
plt.show()