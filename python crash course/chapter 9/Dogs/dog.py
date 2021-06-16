class Dog:
	"""A simple attempt to model a dog."""
	def __init__(self, name, age , breed,color):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		self.breed = breed
		self.color = color

	def get_description(self):
		print(f"\nMy dog's name is {self.name}.")
		print(f"My dog is {self.age} years old.")
		print(f"My dog is a {self.color} {self.breed}.")


	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")


# my_dog = Dog('Lucy', 3, 'Husky','dark brown')
# your_dog=Dog('Spottie',8,'Bulldog','black')
# # manos_dog=Dog('Willie', 6, 'Pitbull','brown and white')


# print(f"My dog's name is {your_dog.name}.")
# print(f"My dog is {your_dog.age} years old.")
# print(f"My dog is a {your_dog.color}  {your_dog.breed}. ")

# your_dog.sit()
# your_dog.roll_over()

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# print(f"My dog is a {my_dog.color} is a {my_dog.breed}.")

# my_dog.sit()
# my_dog.roll_over()



