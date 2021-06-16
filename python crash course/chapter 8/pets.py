def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#def full_name(name,surname):
	#fullName = name + " " + surname
	#print(f"My full name is {fullName.title()}.")

#full_name("lesedi","tumelo")
