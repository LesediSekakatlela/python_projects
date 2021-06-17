import matplotlib.pyplot as plt

values = [16,18,4,8]
pielabels = ['Python','Ruby','Java','Perl']
piecolors = ['blue','gold','lime','purple']
pieexplode = [0.1,0,0,0]#explodes the part of the piechart

plt.pie(values,labels=pielabels,explode=pieexplode,colors=piecolors,startangle=0,shadow=True)
plt.title('Pie Chart')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.legend(loc='best')
plt.show()