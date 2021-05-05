
#pokedex
#create an input that accepts numbers and pokemon names
#plan for if they enter wrong number or name

#main pokemon class

class Pokemon:
    def __init__(self, number, name, type, weight, description):
        self.number = number
        self.name = name
        self.type = type
        self.weight = weight
        self.description = description

#this method will return the data entry for the selected pokemon
    def __repr__(self):
        return self.name + " the " + self.type + " type Pokemon! " + self.description

# these are the different types that a pokemon may be
types = ["Grass", "Fire", "Water", "Electric", "Flying", "Ice", "Dragon", "Poison"]

#this is the instance where we enter the needed pokemon info to complete the class
bulbasaur = Pokemon(1, 'Bulbasaur', types[0], 15.2, "There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger.")


input()
print(bulbasaur)
