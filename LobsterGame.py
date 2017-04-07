import random
from Lobster import Lobster

#######################

# basic "evolving" creature class

#######################
class LobsterGame(object):


    evolutionSuccess = True

    def __init__(self):
        pass

    def play(self):

        lob0wins = 0

        lob1wins = 0

        ticksPerEvolution = 10

        generations = 10

        lob0mutations = 15
        lob1mutations = 50

        # The health gene - your basic, standard lifebar (oh that would be cool - TODO lets animate this)
        lob0health = 10
        lob1health = 10

        lob0 = Lobster(lob0mutations)
        lob1 = Lobster(lob1mutations)

        lob0.name = "Lob0"
        #print("Renamed Lobster 0 to " + lob0.name)

        lob1.name = "Lob1"
        #print("Renamed Lobster 1 to " + lob1.name)

        # A new generation - stats reset, winner gets bonus
        for gen in range(generations):

            for year in range(ticksPerEvolution):

                if lob0.health < 1:
                    lob0.evolveHealth()
                    lob0.health = lob0health
                    #print("EVOLUTION! (also death) " + lob0.name)

                if lob1.health < 1:
                    lob1.evolveHealth()
                    lob1.health = lob1health
                    #print("EVOLUTION! (also death) " + lob1.name)

                lob0.tick()
                lob1.tick()

            #print("Round " + str(gen) + " hps: [" + lob0.name + "," + lob1.name + "] :" + str(lob0.health) + "," + str(lob1.health))



            if lob0.health > lob1.health:
                lob0wins += 1
                lob0health += 1
            else :
                lob1wins += 1
                lob1health += 1

            lob0.health = lob0health
            lob1.health = lob1health
            lob0.life_left = 10
            lob1.life_left = 10


        if lob0wins > lob1wins:
            winner = lob0.name +" , "+ str(lob0wins) + "-" + str(lob1wins)
            winLob = lob0
            loseLob = lob1
        else:
            winner = lob1.name +" , "+ str(lob1wins) + "-" + str(lob0wins)
            winLob = lob1
            loseLob = lob0

        print ("[" + str(lob0.mutation_chance) + "]" + lob0.name),
        print ("vs"),
        print ("[" + str(lob1.mutation_chance) + "]" + lob1.name + " : "),
        print ("Winner = " + winner),

        if (winLob.mutation_chance > loseLob.mutation_chance):
            print ("Evolution won" )
            self.evolutionSuccess = True
        else:
            print ("Evolution lost" )
            self.evolutionSuccess = False





        """"
        print (lob0.name + ":evolutions:" + str(lob0.evolutions))
        print (lob1.name + ":evolutions:" + str(lob1.evolutions))
        print (lob0.name + ":health:" + str(lob0.health))
        print (lob1.name + ":health:" + str(lob1.health))
        print (lob0.name + ":life left:" + str(lob0.life_left))
        print (lob1.name + ":life left:" + str(lob1.life_left))
"""






