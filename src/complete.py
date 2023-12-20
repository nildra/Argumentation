#
# File containing the functions necessary for the implementation of the complete extensions
#

from graphe import Graphe

# def grounded(graphe: Graphe):
#     liste = graphe.arguments
#     for arg in graphe.arguments:
#         for (_, x2) in graphe.relations:
#             if (arg == x2) and (arg in liste):
#                     liste.remove(arg)
#     liste_rouge=[]
#     for arg in liste:
#         for(x1,x3) in graphe.relations:
#             if(x1==arg) and (x3 not in liste_rouge):
#                 liste_rouge.append(x3)
#     for arg in liste_rouge:
#         for (x1, x2) in graphe.relations :
#             if (arg == x1):
#                     liste.append(x2)

#     return liste
# arg =  ['A', 'B', 'C', 'D', 'E'] 
# relation=[('A', 'B'), ('B', 'A'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')]

# g = Graphe(arg,relation)
# print(grounded(g))

def complete(g: Graphe) : 
    # for x, y in g.atk:
    return

''' Returns the list of all argument subsets without conflicts '''
def conflict_free_subsets(g: Graphe):

    ''' Returns True if each of these subsets is conflict-free by ensuring that none of its arguments attack another argument 
        within the same subset; else returns False 
    '''
    def is_conflict_free(subset):
        for arg1 in subset:
            for arg2 in subset:
                if (arg1, arg2) in g.atk or (arg2, arg1) in g.atk:
                    return False
        return True
    
    ''' Returns the list of all possible subsets of arguments '''
    def generate_subsets(args):
        if not args:
            return [[]]
        subsets = generate_subsets(args[1:])
        return subsets + [[args[0]] + subset for subset in subsets]

    all_subsets = generate_subsets(list(g.arguments))
    return [set(subset) for subset in all_subsets if is_conflict_free(subset)]

def admissibles(g: Graphe):
    # prend un arg et ens atk et donne ceux qu'il défend. Puis verifier que ceux qu'il defend fait parti d'un des ens ss conflit
    list_admissibles=[]
    for e in g.arguments:
        x, y = defends(e, g)
        if len(y) == 0:  # Si y est vide on continue
            continue
        else: 
            


            list_admissibles.append(list((x, y)))

    return list_admissibles

''' Returns the list of all the arguments attacked by arg in the Graphe g '''
def attacks(arg, g:Graphe):
    res = []
    for x, y in g.atk:
        if x==arg :
            res += y
    return res

''' Returns the list of all the arguments defended by arg in the Graphe g '''
def defends(arg, g: Graphe):
    res=[]
    for x, y in g.atk:
        if x==arg :
        #verifier si x==y ou deja pris en compte ?
            for x2, y2 in g.atk:
                if y==x2 and y2!=x and y2 not in attacks(arg, g):
                    res += y2
    return (arg, res)
    
   

# public void findCombinaison(int i, int k, Set<ArrayList<Argument>> combinaison, ArrayList<Argument> listeArgument){
#     Argument[]tabArgument= argumentToTab();
#     if (tabArgument.length == 0 || k > tabArgument.length) {
#         return;
#     }
#     if (k == 0) {
#         combinaison.add(new ArrayList<>(listeArgument));
#         return;
#     }
#     for (int j = i; j < tabArgument.length; j++) {
#         listeArgument.add(tabArgument[j]);
#         findCombinaison(j + 1, k - 1, combinaison, listeArgument);
#         listeArgument.remove(listeArgument.size() - 1);
#     }
# }

