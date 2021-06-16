#project 1

import random

health = 50

# #defining a variable set it to easy, 1 = easy , 2 = medium , 3 = hard
difficulty = 1

#creating a potion randomly with variables 
potion_health = int(random.randint(25,50) / difficulty)

#box = health
#storing the current health to the + the potion_health
health = health + potion_health

#built in python function (print)
print(health)
