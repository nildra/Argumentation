#
# File containing the functions necessary for the implementation of the complete extensions
#

from graphe import Graphe

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
    return [list(subset) for subset in all_subsets if is_conflict_free(subset)]

''' Returns the list of all the admissible arguments subsets in the Graphe g '''
def admissibles(g: Graphe):
    conflict_free = conflict_free_subsets(g)
    admissible_sets = []

    for subset in conflict_free:
        is_admissible = True
        for arg in subset:
            for attacker in [a for a, b in g.atk if b == arg]:
                if attacker not in subset and not any((defender, attacker) in g.atk for defender in subset):
                    is_admissible = False
                    break

        if is_admissible:
            admissible_sets.append(subset)

    return admissible_sets

''' Returns a list of arguments that are attacked by the subset given as a parameter '''
def arguments_attacked_by_subset(g: Graphe, subset):
    attacked = set()
    for x, y in g.atk:
        if x in subset:
            attacked.add(y)
    return list(attacked)

''' Returns a list of arguments that attack the subset given in the parameter '''
def attackers_of_the_subset(g: Graphe, subset):
    attackers = set()
    for x, y in g.atk:
        if y in subset and x not in subset:
            attackers.add(x)
    return list(attackers)

''' Returns True if a subset of arguments given in parameter is a complete extension, else returns False '''
def is_complete(g: Graphe, subset):
    attacked = arguments_attacked_by_subset(g, subset)  
    '''Returns True if all the arguments that subset defends are part of subset.'''
    def check_internal_defense(subset):
        res = []
        for arg in g.arguments:
            attackers = attackers_of_the_subset(g, arg)
            if set(attackers).issubset(attacked) : 
                res.append(arg)
        if set(res).issubset(subset) :
            return True
        return False
    ''' Returns True if the subset defends all its members against external attacks.'''
    def verify_inclusion_defense(subset):
        for arg in subset: 
            attackers= attackers_of_the_subset(g, arg) 
            if not set(attackers).issubset(attacked) :
                return False
        return True
    return check_internal_defense(subset) and verify_inclusion_defense(subset)

''' Generates the list of complete subsets ''' 
def complete(g: Graphe):
    complet = []
    for subet in admissibles(g): 
        if is_complete(g, subet): 
            complet.append(subet)
    return complet


''' Returns True if a set of arguments 'solution' is complete 
    Sorts the set given in parameter and the complete subsets to simplify comparison
'''
def VE_CO(g:Graphe,solution):
    tab_sol = sorted(solution.split(","))
    for sol in complete(g):
        if tab_sol[0] == '[]' and len(sol) == 0 : #if the empty set '[]' is given in command line parameter
            return True 
        if (sorted(sol) == tab_sol):
            return True
    return False