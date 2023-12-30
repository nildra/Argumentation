#
# File containing the functions necessary for the implementation of the stable extensions
#
from graphe import Graphe
from complete import *

''' Returns the list of all the stable extensions in the Graphe 'g'
    An extension is stable if it's conflict free and attacks all the arguments that are not in the extension
'''
def stable(g: Graphe):
    stable=[]
    conflict_free= conflict_free_subsets(g)
    for s in conflict_free:
        if is_stable(s,g):
            stable.append(s)

    return stable

''' Verify the second part of the definition of a stable extension : 
    the extensions attack all the arguments that are not in the extension
'''  
def is_stable(S,g:Graphe):
    attaque_all=True
    for aj in g.arguments:
        if aj not in S:
            attaque_trouve=False
            for ak in S:
                if(ak,aj) in g.atk:
                    attaque_trouve=True
                    break
            if not attaque_trouve:
                attaque_all=False
                break
    return attaque_all

''' Returns True if a set of arguments 'solution' is stable 
    Sorts the set given in parameter and the complete subsets to simplify comparison
'''
def VE_ST(g:Graphe,solution):
    tab_sol = sorted(solution.split(","))
    for sol in stable(g):
        if tab_sol[0] == '[]' and len(sol) == 0 : #if the empty set '[]' is given in command line parameter
            return True 
        if (sorted(sol) == tab_sol):
            return True
    return False

