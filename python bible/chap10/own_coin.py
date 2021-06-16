#part 1

#A class is a template
class Pound:

	
	value = 1.00
	colour = "gold"
	num_edges = 1
	diameter = 22.5 #mm
	thickness = 3.15 #mm
	heads = True 

#objects are instants 
coin1 = Pound()
print(coin1.value)

coin1.colour = "greenish"
print(coin1.colour)

coin2 = Pound()

print(coin2.colour)

coin1.value = 1.25
print(coin1.value)

print(coin2.value)

#part 2

class Pound:
    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True 

    def rust(self):
    	self.colour = "greenish"

coin1 = Pound(rare=True)
coin2 = Pound()
print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)

coin1 = Pound()
coin2 = Pound()
print(coin1.colour)

[1,2,3,4].append(5)
coin1.rust()
print(coin1.colour)
print(coin2.colour)