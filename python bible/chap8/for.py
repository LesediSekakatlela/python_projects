#using a forloop using range
#range(1,11)
for p in range(1,11):
    print(p)

#increment the sequence
for t in range(2,20,3):
    print(t)



students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

