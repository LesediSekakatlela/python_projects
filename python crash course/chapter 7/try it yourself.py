#7-1

message = input("Tell me which car you want to rent,and I will display it:")
print(message)




#7-2

question = "How many people in your group?"

number= input(question)
number= int(number)
if number <=8:
 	print(f"The number {number} is low. Your table is ready!")
else:
	print(f"The number {number} is too high.Wait for a nother table!")




#7-3


number = input("Enter a number, and I'll tell you if it's a multiple of 10 or not: ")
number = int(number)


if number % 2 == 0:
	print(f"\nThe number {number} is multiple.")
else:
	print(f"\nThe number {number} is not a multiple.")



#7-4


prompt = "\nPlease enter the name of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	pizza = input(prompt)
	if pizza == 'quit' :
		break
	else:
		print(f"I love this flavours {pizza.title()}!")


#7-5


question = "How old are you?"

age= input(question)
age= int(age)
if age >= 12:
 	print(f"The age {age} the ticket is $15!")
else:
 	print(f"The age {age} the ticket is free!")




#7-6


#7-8

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
sandwiches_order = ['tuna sandwich', 'cheese sandwich', 'muchroom sandwich']
finished_sandwiches = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of comfirmed users.
while sandwiches_order:
	current_user = sandwiches_order.pop()
	print(f"Verifying user: {current_user.title()}")
	finished_sandwiches.append(current_user)


# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for finished_sandwiches in finished_sandwiches:
	print(finished_sandwiches.title())


#7-9


#7-10
message = input("Tell me which vaction home you want to visit,and I will display it:")
print(message)


responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which vaction home would you loke to visit? ")

	# Store the response in the dictionary.
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")