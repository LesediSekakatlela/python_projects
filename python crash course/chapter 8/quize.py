def display_message(username):
	"""Display a simple sentence."""
	print(f"Coding, {username.title()}! ")

display_message('in this program im learning how to code')



#8-2


def favorite_book(book_type):
	"""Display information about the book."""
	print(f"\n One of my favorite books is The Walking Dead")








#8-3



def make_shirt(shirt_type, size_number):
	"""Display information about the shirt."""
	print(f"\nI have a {shirt_type} shirt.")
	print(f"The size of my shi is  {size_number} and its  {shirt_type.title()}.")

make_shirt('blue', '12')




#8-6


def city_country(city_name, country_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{city_name} {country_name}"
	return full_name.title()

place = city_country('bloemfontein', 'south africa')
print(place)

#8-9
def show_message(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['ben', 'lee', 'ten']
show_message(usernames)

#8-10
# Start with some messages that need to be printed.
send_messages = ['popcorns', 'chocolates', 'candy']
sent_messages = []

# Simulate printing each message, until none are left.
# Move each message to sent_messages after printing.
while send_messages:
	current_messages = send_messages.pop()
	print(f"Printing model: {current_messages}")
	sent_messages.append(current_messages)

# Display all sent_messages
print("\nThe following models have been printed:")
for sent_messages in sent_messages:
	print(sent_messages)

def show_message(send_messages, sent_messages):
	"""
	Simulate printing each design, until none are left.
	Move each design to sent_messages after printing.
	"""
	while send_messages:
		current_messages =send_messages.pop()
		print(f"Printing model: {current_messages}")
		sent_messages.append(current_messages)

def show_sent_messages(sent_messages):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for sent_message in sent_messages:
		print(sent_messages)

send_messages= ['popcorns', 'chocolates', 'candy']
sent_messages = []

show_message(send_messages[:], sent_messages)
show_sent_messages(sent_messages)


#8-12
def make_sandwiches(size,*flavors):
	"""Summarize the sandwiches we are about to make."""
	print(f"\nMaking a {size}-inch sandwich with the following flavors:")
	for flavors in flavors:
		print(f"- {flavors}")

make_sandwiches(14,'cheese sandwich')
make_sandwiches(10,'ham ', 'backon and egg', 'tuna ')

#8-13
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('lesedi', 'tumelo',
							location='south africa',
							field='coding')
print(user_profile)

#8-14
def make_car(car_name,model_name, color_name,tow_package):
	"""Display information about a pet."""
	print(f"\nI have a {car_name}.")
	print(f"Its a {model_name}.")
	print(f"There is a tow_package {tow_package}.")
	print(f"My car  {car_name} is {color_name.title()}.")

make_car(car_name='toyota', model_name='outback',color_name= 'blue',tow_package='True')