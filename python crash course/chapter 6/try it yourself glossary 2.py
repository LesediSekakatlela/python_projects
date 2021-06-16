#6-4


favorite_language={
	'kat' : 'science', 
	'sam' : 'pyton',
	'jack' : 'ruby',
	'lola' : 'science',
	'pearl' : 'math',
}


for name in sorted(favorite_language.keys()):
	print(f" {name.title()}, thank you for taking the poll.")



#6-5


the_river = {
	' nile river' : 'egypt'
}

for name in sorted(the_river.keys()):
	print(f" {name.title()},the nile runs through egypt")





	#6-6


favorite_language={
	'kat' : 'science', 
	'sam' : 'pyton',
	'jack' : 'ruby',
	'lola' : 'science',
	'pearl' : 'math',
}


for name in sorted(favorite_language.keys()):
	print(f" {name.title()}, thank you for taking the poll.")


#6-7


people = {
	'wsmith': {
		'first': 'will',
		'last': 'ssmith',
		'location': 'america',
		},
	'bknowls': {
		'first': 'beyonce',
		'last': 'knowls',
		'location': 'america',
		},
	}

for username, people_info in people.items():
	print(f"\nUsername: {username}")
	full_name = f"{people_info['first']} {people_info['last']}"
	location = people_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")



#6-8

