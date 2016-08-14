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
        return math.ceil(rofl//100) * 100

    #N/A
    else:
        return "Sorry, that is not a valid response."


print "Yo what\'s up, mate?"

cap = raw_input("How much exp do you need in total to level up?")
accumulated = raw_input("How much exp have you accumulated so far?")
expneeded = int(cap) - int(accumulated)


print "Ok, so you'll need to catch %s more pokemon or evolve %s more pokemon." % (rtnh(expneeded)/100, rtnh(expneeded)/500)


















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
