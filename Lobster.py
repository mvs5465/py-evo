import os
import random

class Lobster(object):

    def __init__(self, mutation_chance):

        self.evolutions = 0

        names = ["Ali", "Bob", "Car", "Dud"]

        self.name = names[random.randint(0,3)] + str(mutation_chance)

        self.life_left = 10

        self.health = 10

        self.mutation_chance = mutation_chance

        #print("New lobster: " + self.name)

    def tick(self):

        #self.drawHealth()

        if self.health < 1:
            print(self.name + " ran out of health.")

        if self.life_left < 1:
            print(self.name + " SENTINEL... [error - you shouldn't be seeing this message]") # just for fun
            return

        self.life_left -= 1

        healthkick = random.randint(-self.mutation_chance, self.mutation_chance) # favors positive evolution

        #print(self.name + " :healthkick: " + str(healthkick))

        self.health += healthkick

    def evolveHealth(self):

        self.evolutions += 1
        self.life_left = 10 # i guess i should make this global lol
        self.mutation_chance += 1



    def drawHealth(self):

        #os.system('clear')

        for count in range(self.health):
            print("  ==  ")

        print("_______")





