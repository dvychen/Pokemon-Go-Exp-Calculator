import math

def rtnh(rofl):
    #One digit / two digits
    if rofl > 0 and rofl < 10:
        return 100
    #Three digits or more
    elif rofl > 99:
        return math.ceil(rofl/100) * 100

    #N/A
    else:
        return 404

#Constants
CANDY_PER_PK = 4
EXP_FROM_EVOLUTION = 500

print "Welcome to the Pokemon Go Exp Calculator!"
print "Main Menu"
print "1. Basic/Got all the candy"
print "2. Smart/Catching and Evolving one Pokemon"
choice = raw_input("Which mode would you like to use? ").lower()


cap = raw_input("How much exp do you need in total to level up? ")
accumulated = raw_input("How much exp have you accumulated so far? ")
expneeded = rtnh(int(cap) - int(accumulated))


#Variables for choice 1 (Basic/Got all the candy)
pktoevolve = rtnh(expneeded) // EXP_FROM_EVOLUTION
pktocatch = rtnh(expneeded) / 100

lol = rtnh(expneeded) % EXP_FROM_EVOLUTION
pktosituational = lol / 100



if int(cap) < int(accumulated):
    print "Sorry, you could not have accumulated %s exp if you needed %s exp in total." % (accumulated, cap)
else:
    if choice == "basic" or choice == "got all the candy" or choice == "basic/got all the candy" or choice == "1. basic/got all the candy" or choice == "1":
        if rtnh(expneeded) % EXP_FROM_EVOLUTION == 0:
            print "Ok, so you\'ll need to catch %s more pokemon or evolve/discover %s more pokemon." % (pktocatch, pktoevolve)
        elif rtnh(expneeded) % EXP_FROM_EVOLUTION != 0 and pktoevolve != 0:
            print "Ok, so you\'ll need to catch %s more pokemon or catch %s more pokemon and evolve/discover %s pokemon." % (pktocatch, pktosituational, pktoevolve)
        elif pktoevolve < 0:
            print "Ok, so you\'ll need to catch %s more pokemon." % (pktocatch)
        else:
            print "Sorry, that is not a valid choice!"
    
    
    elif choice == "smart" or choice == "catching and evolving one pokemon" or choice == "smart/catching and evolving one pokemon" or choice == "2. smart/catching and evolving one pokemon" or choice == "2":
        candiesneeded = raw_input("How many candies do you need per evolution? ")
        
        zed = int(candiesneeded)
        z_over_four = zed//CANDY_PER_PK + zed % CANDY_PER_PK
        exp_from_z_over_four = z_over_four * 100 + EXP_FROM_EVOLUTION
        
        
        pktoevolve_smart = expneeded // exp_from_z_over_four
        extrapktocatch = (expneeded % exp_from_z_over_four)/100
        
        pktocatch_smart = pktoevolve_smart * z_over_four + extrapktocatch
        
        print "Ok, so you\'ll need to catch %s more pokemon and evolve %s of them." % (pktocatch_smart, pktoevolve_smart)
        
        if pktocatch_smart > pktoevolve_smart and pktoevolve_smart >= 0:
            print "Ok, so you\'ll need to catch %s more pokemon and evolve %s of them." % (pktocatch_smart, pktoevolve_smart)
        else:
            print "Oops, something went wrong! Please contact me to fix this."
    else:
        print "Sorry, that is not a valid mode."
        
    
