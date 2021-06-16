#counting a string

#pull out the first letter
a = "supercalifragilisticexpialidocious"
print(a[0])

#using a slice
#variable[start:end:step]
print(a[0:5:1])

#changing the step value skips one letter 
print(a[0:5:2])

#using a slice to take out cali
print(a[5:9:1])

#from letter c to the end
print(a[5:])

#from letter c skipping two
print(a[5::2])

#only up to 8
print(a[:8])

#reverse the string
print(a[::-1])

#the ending value
print(a[-5])

#using index
word = "supercalifragilisticexpialidocious"

x = word.index("cali")
print(x)

#upper() and lower() case

a = "Hello, World!"
print(a.upper())

a = "Hello,World!"
print(a.lower())