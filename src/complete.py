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

def complete(g: Graphe):
    admissible_sets = admissibles(g)
    complete_extensions = []

    for candidate in admissible_sets:
        # Un ensemble est considéré comme complet s'il n'existe pas d'ensemble admissible qui le contient strictement.
        is_maximal = not any(candidate.issubset(other) and candidate != other for other in admissible_sets)
        if is_maximal:
            complete_extensions.append(candidate)

    # Ajouter l'ensemble vide si c'est une extension complète
    if all(not any((defender, attacker) in g.atk for defender in set()) for _, attacker in g.atk):
        complete_extensions.append(set())

    return complete_extensions



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

''' Returns the list of all the admissible arguments subsets in the Graphe g '''
def admissibles(g: Graphe):
    conflict_free = conflict_free_subsets(g)
    admissible_sets = []

    for subset in conflict_free:
        is_admissible = True
        for arg in subset:
            # Vérifier si l'argument est attaqué par un argument extérieur au sous-ensemble
            for attacker in [a for a, b in g.atk if b == arg]:
                # Si l'attaquant n'est pas dans le sous-ensemble, vérifier si un défenseur dans le sous-ensemble peut contrer l'attaque
                if attacker not in subset and not any((defender, attacker) in g.atk for defender in subset):
                    is_admissible = False
                    break

        if is_admissible:
            admissible_sets.append(subset)

    return admissible_sets


''' Returns the list of all the arguments attacked by arg in the Graphe g '''
def attacks(arg, g:Graphe):
    return [y for x, y in g.atk if x == arg]

''' Returns the list of all the arguments defended by arg in the Graphe g '''
def defends(arg, g: Graphe):
    defended = []
    for x, y in g.atk:
        if x == arg:
            for x2, y2 in g.atk:
                if y == x2 and y2 != x and y2 not in attacks(arg, g):
                    defended.append(y2)
    return (arg, defended)
    
   

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


''' Returns True if a set of arguments 'solution' is complete '''
def VE_CO(g:Graphe,solution):
    complete_g = complete(g)
    response = False
    for sol in complete_g:
        if (sol==solution):
            response=True
    return response