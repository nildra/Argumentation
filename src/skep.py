from graphe import Graphe
from stable import *
from complete import complete

''' Returns the list of the skeptically accepted arguments '''
def skeptical(solutions,arguments):
    result=[]
    for arg in arguments:
        if all(arg in solution for solution in solutions ):
            result.append(arg)
    return result

''' Returns True if an argument 'arg' is skeptically accepted in a stable extension, else False '''
def DS_ST(g: Graphe,arg):
    response = False
    stable_g=stable(g)
    skep_g=skeptical(stable_g,g.arguments)
    for a in skep_g:
        if(a==arg):
            response = True
    return response

''' Returns True if an argument 'arg' is skeptically accepted in a complete extension, else False '''
def DS_CO(g: Graphe,arg):
    response = False
    complete_g=complete(g)
    skep_g=skeptical(complete_g,g.arguments)
    for a in skep_g:
        if(a==arg):
            response = True
    return response