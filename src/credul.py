from graphe import Graphe
from stable import *
from complete import *

''' Returns the list of the credulously accepted arguments '''
def credul(solutions, arguments):
    result =[]
    for arg in arguments:
        for sol in solutions :
            if (arg in sol) and (not (arg in result)):
                result.append(arg)
                break

    return result

''' Returns True if an argument 'arg' is credously accepted in a stable extension, else False '''
def DC_ST(g:Graphe,arg):
    stable_g=stable(g)
    cred_g=credul(stable_g,g.arguments)
    response =False
    for a in cred_g:
        if (a==arg):
            response = True
    return response

''' Returns True if an argument 'arg' is credously accepted in a complete extension, else False '''
def DC_CO(g:Graphe,arg):
    complete_g=complete(g)
    cred_g=credul(complete_g,g.arguments)
    response =False
    for a in cred_g:
        if (a==arg):
            response = True
    return response