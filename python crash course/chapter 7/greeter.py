#name = input("Please enter your name:")
#print(f"\nHello, {name}!")

question = "How old are you?"

age= input(question)
age= int(age)
if age >= 18:
	print(f"The age {age} is old enough. You may enter!")
else:
	print(f"The age {age} is not old enough. Go home!")