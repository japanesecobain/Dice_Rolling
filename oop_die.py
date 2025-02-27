import random
'''Aoi Araki'''

class Die:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.roll()
    
    def roll(self):
        self.current_face = random.randint(1, self.number_of_sides)
        return self.current_face
    
    def __str__(self):
        return f"D{self.number_of_sides}: {self.current_face}"

    def __repr__(self):
        return f"Die(number_of_sides={self.number_of_sides})"

    def __add__(self, die):
        return self.current_face + die.current_face

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.skip_turn = False

    def update_the_score(self, number):
        self.score += number
    

    def main():
        num_players = int(input("Enter the number of players (2 or more): "))
        while num_players < 2:
            num_players = int(input("Please enter at least 2 players: "))
    
        players = []
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            players.append(Player(name))    

# I forgot how to shuffle things but I need a shuffling method here.

my_die = Die(6)
my_second_die = Die(12)
print("Initial Face (D6):", my_die.current_face)
print("Initial Face (D12):", my_second_die.current_face)
print("Rolled (D6):", my_die.roll())
print("Rolled (D12):", my_second_die.roll())
print("New Face (D6):", my_die.current_face)
print("New Face (D12):", my_second_die.current_face)

my_str = "Hello"
print(str(my_str))
print(repr(my_str))

my_list = {Die(5), Die(5)}
print(my_list)

print("Total is", my_die + my_second_die)
#Standard Conventions
#__str__ : For Humans(Users)
#__repr__: For Programmers(Programmers), Programmer manually calls it, or a list or a collection of a type is printed. 
#Quotes are for repr, and not for strings
#You can tell python not to do something, but to do something else
