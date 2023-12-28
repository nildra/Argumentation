from graphe import Graphe
from stable import *
from complete import *

def credul(solutions, arguments):
    result =[]
    for arg in arguments:
        for sol in solutions :
            if (arg in sol) and (not (arg in result)):
                result.append(arg)
                break

    return result

#Verify if an argument is credously accepted in stable extension
def DC_ST(g:Graphe,arg):
    stable_g=stable(g)
    cred_g=credul(stable_g,g.arguments)
    response =False
    for a in cred_g:
        if (a==arg):
            response = True
    return response

#Verify if an argument is credously accepted in complete extension
def DC_CO(g:Graphe,arg):
    complete_g=complete(g)
    cred_g=credul(complete_g,g.arguments)
    response =False
    for a in cred_g:
        if (a==arg):
            response = True
    return response