#3-4

dinner = ['mary' , 'kim' ,'jacob']
print(dinner)


print(dinner[0])
print(dinner[1])
print(dinner[2])


message = f"Come join me for dinner {dinner[0].title()}."
print(message)
message = f"I'm hosting a dinner party hope you make it {dinner[1].title()}."
print(message)
message = f"Hello i hope your free i'm having a dinner party today {dinner[2].title()}."
print(message)

#3-5

dinner.remove('jacob')
print(dinner)

dinner = ['mary' , 'kim' ,'max']
print(dinner)

message = f"Come join me for dinner {dinner[0].title()}."
print(message)
message = f"I'm hosting a dinner party hope you make it {dinner[1].title()}."
print(message)
message = f"Hello sorry for the last minutes text but i'm having a dinner party hope you will make it {dinner[2].title()}."
print(message)


#3-6

dinner.insert(0,   'chris')
print(dinner)

