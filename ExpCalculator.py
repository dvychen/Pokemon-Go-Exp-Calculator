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
        return "Sorry, that is not a valid response."


print "Welcome to the Pokemon Go Exp Calculator!"
print "Main Menu"
print "1. Basic/Got all the candy"
print "2. Smart/Catching and Evolving one Pokemon"
choice = raw_input("Which mode would you like to use?"


cap = raw_input("How much exp do you need in total to level up?")
accumulated = raw_input("How much exp have you accumulated so far?")
expneeded = int(cap) - int(accumulated)

pktoevolve = rtnh(expneeded) // 500
pktocatch = rtnh(expneeded) / 100

lol = rtnh(expneeded) % 500
pktosituational = lol / 100


if choice == "Basic" or choice == "Got all the candy" or choice == "Basic/Got all the candy" or choice == "1. Basic/Got all the candy" or choice == "1":
    if rtnh(expneeded) % 500 == 0:
        print "Ok, so you'll need to catch %s more pokemon or evolve/discover %s more pokemon." % (pktocatch, pktoevolve)
    elif rtnh(expneeded) % 500 != 0 and pktoevolve != 0:
        print "Ok, so you'll need to catch %s more pokemon or catch %s more pokemon and evolve/discover %s pokemon." % (pktocatch, pktosituational, pktoevolve)
    elif rtnh(expneeded) % 500 != 0 and pktoevolve == 0:
        print "Ok, so you'll need to catch %s more pokemon." % (pktocatch)

elif choice == "Smart" or choice == "Catching and evolving one Pokemon" choice == "Smart/Catching and Evolving one Pokemon" or choice == "2. Smart/Catching and Evolving one Pokemon" or choice == "2":
    if rtnh(expneeded) % 500 == 0:
        print "
    elif rtnh(expneeded) % 500 != 0 and pktoevolve != 0:
        print "
    elif rtnh(expneeded) % 500 != 0 and pktoevolve == 0:
        print "
    






"""
Note to self:
Add a "menu" that let's you choose which mode;
-Current one (most efficient way)
-One where you only catch one type of pokemon, displaying as if you transfer all the pokemon and evolve only that type

Add more!
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
