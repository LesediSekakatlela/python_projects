# def sum(val1 ,val2):
#  	total = val1 + val2
#  	print(f"The sum of {val1} and {val2} is: {total}")


# sum(15,15)


# def sum(val1,val2,val3):
#  	total = val1 + val2 + val3
#  	print(f"The sum of {val1} and {val2} and {val3}")


def get_formatted_name(first_name, last_name):
 	"""Return a full name, neatly formatted."""
 	full_name = f"{first_name} {last_name}"
 	return full_name.title()

 #This is an infinite loop!
while True:
	print("Please tell me your name.\nOr enter 'q' to quit.\n")
	f_name = input("First_name: ")
	l_name = input("Last_name: ")
	formatted_name = get_formatted_name(f_name, l_name)
	if (f_name or l_name) == 'q':
		break
	else:
		print(f"\nHello, {formatted_name}!\n")