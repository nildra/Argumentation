from graphe import Graphe


def grounded(graphe: Graphe):
    liste = graphe.arguments
    for arg in graphe.arguments:
        for (_, x2) in graphe.relations:
            if (arg == x2) and (arg in liste):
                    liste.remove(arg)
    liste_rouge=[]
    for arg in liste:
        for(x1,x3) in graphe.relations:
            if(x1==arg) and (x3 not in liste_rouge):
                liste_rouge.append(x3)
    for arg in liste_rouge:
        for (x1, x2) in graphe.relations :
            if (arg == x1):
                    liste.append(x2)

    return liste
# arg =  ['A', 'B', 'C', 'D', 'E'] 
# relation=[('A', 'B'), ('B', 'A'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')]

# g = Graphe(arg,relation)
# print(grounded(g))

