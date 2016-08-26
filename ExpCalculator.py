import math

def rtnh(rofl):
    #One digit
    if rofl > 0 and rofl < 10:
        return 100
    #Two digits
    elif rofl > 9 and rofl < 100:
        return 100
    #Three digits
    elif rofl > 99:
        return math.ceil(rofl/100) * 100

    #N/A
    else:
        return "ERROR"


print "Welcome to the Pokemon Go Exp Calculator!"
print "Main Menu"
print "1. Basic/Got all the candy"
print "2. Smart/Catching and Evolving one Pokemon"
choice = raw_input("Which mode would you like to use? ")


cap = raw_input("How much exp do you need in total to level up? ")
accumulated = raw_input("How much exp have you accumulated so far? ")
expneeded = int(cap) - int(accumulated)



#Variables for choice 1 (Basic/Got all the candy)
pktoevolve = rtnh(expneeded) // 500
pktocatch = rtnh(expneeded) / 100

lol = rtnh(expneeded) % 500
pktosituational = lol / 100

#Variables for choice 2 (Smart/Catching one type of pokemon)
fistep = rtnh(expneeded)
#sestep is how many pokemon to catch, ex: 4800exp --> 48 pokemon to catch
sestep = fistep/100
#thstep and thpofistep are useless here, just filler, may remove later
thstep = sestep//5
thpofistep = sestep % 5

if int(cap) < int(accumulated):
    print "Sorry, you could not have accumulated %s exp if you needed %s exp in total." % (accumulated, cap)
elif int(cap) >= int(accumulated):
    if choice == "Basic" or choice == "Got all the candy" or choice == "Basic/Got all the candy" or choice == "1. Basic/Got all the candy" or choice == "1":
        if rtnh(expneeded) % 500 == 0:
            print "Ok, so you\'ll need to catch %s more pokemon or evolve/discover %s more pokemon." % (pktocatch, pktoevolve)
        elif rtnh(expneeded) % 500 != 0 and pktoevolve != 0:
            print "Ok, so you\'ll need to catch %s more pokemon or catch %s more pokemon and evolve/discover %s pokemon." % (pktocatch, pktosituational, pktoevolve)
        elif pktoevolve < 0:
            print "Ok, so you\'ll need to catch %s more pokemon." % (pktocatch)
        else:
            print "Sorry, that is not a valid choice!"
    
    
    elif choice == "Smart" or choice == "Catching and evolving one Pokemon" or choice == "Smart/Catching and Evolving one Pokemon" or choice == "2. Smart/Catching and Evolving one Pokemon" or choice == "2":
        candiesneeded = raw_input("How many candies do you need per evolution? ")
        candiesneeded_lol = int(candiesneeded)
        
        pktocatchtoevolve = candiesneeded_lol/4
        thstep = sestep//pktocatchtoevolve
        fostep = thstep + 1
        fifstep = sestep/fostep
        sistep = sestep/fifstep
        sevstep = sestep % fifstep
        
        
        pktocatchtwo = fifstep * thstep + sevstep
        pktoevolvetwo = fifstep
        
        if pktocatchtwo > pktoevolve and pktoevolve >= 0:
            print "Ok, so you\'ll need to catch %s more pokemon and evolve %s of them." % (pktocatchtwo, pktoevolvetwo)
        else:
            print "Oops, something went wrong! Please contact me to fix this."
    else:
        print "Sorry, that is not a valid mode."
        
    
    








"""
Note to self:
Add a "menu" that let's you choose which mode;
-Current one (most efficient way)
-One where you only catch one type of pokemon, displaying as if you transfer all the pokemon and evolve only that type
-One where calculates how many more of pokemon you'll need to catch to evolve into final evolution (counting 4 per catch and
transfering ALL the ones currently possess / choosing how many of current to transfer)
Add more!


MAKE IT SO IT TAKES THE ANSWER CHOICE OF MODE DE-CAPITALIZED SO IT DOES NOT MATTER HOW THE CAPITILIZATION IS!!

Eventually insert number of candies needed to evolve a pokemon, like they insert a pokemon, and code accesses databank and 
finds the right number of candies for that pokemon to evolve.
example:
pokename = raw_input("What pokemon will you be catching?")
pokedict = {"Rattata", "Pidgey", "Weedle"...}
pokemon_list_candy = [12, 25, 50...]
if 
"""




""" How to tell how many digits
#One digit
    if rofl > 0 and rofl < 10:
        return
#Two digits
    elif rofl > 9 and rofl < 100:
        return
#Three digits
    elif rofl > 99 and rofl < 1000:
        return
#Four digits
    elif rofl > 999 and rofl < 10000:
        return
#Five digits
    elif rofl > 9999 and rofl < 100000:
        return
#Six digits
    elif rofl > 99999 and rofl < 1000000:
        return
#N/A
    else:
        return "Sorry, that is not a valid response."
"""
