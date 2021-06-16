# alien_0 = {'color':'brown' , 'speed' : 'medium',}

# point_value = alien_0.get('points', 'No point key assigned.')
# print(point_value)


people = {'firstName' :'Will','lastName':'Smith','age' : 50}
print(f"Name: {person['firstName']} {person['lastName']}")
point_value = person.get('email', 'No email value assigned.')
print(point_value)
#for name,language in favorite_language.item():
#	print(f"{name.title()}'s favorite_language is {language.title()}.")

for k, v in person.items():
	print(f"\nKey: {k}")
	print(f"Value: {v}")