#
# File containing the functions necessary for the implementation of the stable extensions
#
from graphe import Graphe
from complete import *


# verify the second part of the definition of a stable extension : the extension attack all arguments if they are not in the extension 
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


# an extension is stable if it is conflict free and attack all arguments they are not in the extension
# return a list of the stable extension of a graph
def stable(g: Graphe):
    stable=[]
    conflict_free= conflict_free_subsets(g)
    for s in conflict_free:
        if is_stable(s,g):
            stable.append(s)

    return stable

# Verify if a set of arguments is stable
def VE_ST(g:Graphe,solution):
    stable_g = stable(g)
    response = False
    for sol in stable_g:
        if (sol==solution):
            response=True
    return response

