from graphe import Graphe
from stable import *
from complete import complete


def skeptical(solutions,arguments):
    result=[]
    for arg in arguments:
        if all(arg in solution for solution in solutions ):
            result.append(arg)
    return result

#Verify if an argument is skepticaly accepted in stable extension
def DS_ST(g: Graphe,arg):
    response = False
    stable_g=stable(g)
    skep_g=skeptical(stable_g,g.arguments)
    for a in skep_g:
        if(a==arg):
            response = True
    return response

#Verify if an argument is skepticaly accepted in complete extension
def DS_CO(g: Graphe,arg):
    response = False
    complete_g=complete(g)
    skep_g=skeptical(complete_g,g.arguments)
    for a in skep_g:
        if(a==arg):
            response = True
    return response