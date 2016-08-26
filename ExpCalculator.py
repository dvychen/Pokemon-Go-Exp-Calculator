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
        return 404


print "Welcome to the Pokemon Go Exp Calculator!"
print "Main Menu"
print "1. Basic/Got all the candy"
print "2. Smart/Catching and Evolving one Pokemon"
choice = raw_input("Which mode would you like to use? ")


cap = raw_input("How much exp do you need in total to level up? ")
accumulated = raw_input("How much exp have you accumulated so far? ")
expneeded = int(cap) - int(accumulated)
expneeded = rtnh(expneeded)


#Variables for choice 1 (Basic/Got all the candy)
pktoevolve = rtnh(expneeded) // 500
pktocatch = rtnh(expneeded) / 100

lol = rtnh(expneeded) % 500
pktosituational = lol / 100

#Variables for choice 2 (Smart/Catching one type of pokemon)


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
        zed = int(candiesneeded)
        
        z_over_four = zed//4 + zed % 4
        exp_from_z_over_four = z_over_four * 100 + 500
        
        
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
        
    
