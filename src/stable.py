#
# File containing the functions necessary for the implementation of the stable extensions
#
from graphe import Graphe
from complete import *

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

    return
def stable(g: Graphe):
    stable=[]
    conflict_free= conflict_free_subsets(g)
    for s in conflict_free:
        if is_stable(s,g):
            stable.append(s)

    return stable

arg =  ['A', 'B', 'C', 'D', 'E'] 
relation=[('A', 'B'), ('B', 'A'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'D')]
g = Graphe(arg,relation)
print(stable(g))