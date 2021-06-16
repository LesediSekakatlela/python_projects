class Restaurant:
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, food,year ):
		"""Initialize name and age attributes."""
		self.name = name
		self.food = food
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.name} {self.food}"
		return long_name.title()

my_new_restaurant = Restaurant('big lee', 'burgers', 2019)
print(my_new_restaurant.get_descriptive_name())


#9-2


