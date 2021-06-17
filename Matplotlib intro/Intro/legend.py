import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'go-', label = 'students')
plt.plot(x1, y2, 'b^-', label = 'teachers')


# plt.legend(loc='best')can be changed to other values e.g 'upper right'
plt.subplots_adjust(right=0.7, bottom=0.3)#make it smaller
plt.legend(bbox_to_anchor=(1.05,1))#moves the legend

plt.title('Playground')
plt.xlabel('Horizontal')
plt.ylabel('Vertical')
plt.grid(True)
plt.show()