# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = f"{first_name} {last_name}"
# 	return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
# 	"""Return a full name, neatly formatted."""
# 	if middle_name:
# 		full_name = f"{first_name} {middle_name} {last_name}"
# 	else:
# 		full_name = f"{first_name}  {last_name}"
# 	return full_name.title()

#musician = get_formatted_name('john', 'lee', 'hooker')
#print(musician)



#This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit) ")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	m_name = input("Middle name:")
	if m_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name, m_name)
print(f"\nHello, {formatted_name}!")