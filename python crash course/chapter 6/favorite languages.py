# favorite_language = {
# 	'jen' : 'python',
# 	'sarah' : 'c',
# 	'edward' : 'ruby',
# 	'phil' : 'python',
# }



# print('Key-value pairs:')
# for name, language in favorite_language.items():
# 	print(f"\t{name.title()}'s favorite language is {language.title()}.")

# print('\nKeys:')
# for name in favorite_language.keys():
# 	print(f"\t{name.title()}")

# print('\nValues:')
# for language in favorite_language.values():
# 	print(f"\n{language.title()}")


favorite_language = {
 	'jen': ['python', 'ruby', 'javascript'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")



# friends = ['phil','sarah']
# for name in favorite_language.key():
# 	print(name.title())
# 	if name in friends:
# 		language = favorite_language[name].title()
# 		print(f"\t{name.title()}, I see you love {language}!")