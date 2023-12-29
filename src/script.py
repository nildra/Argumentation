#
# Main file
#

import os
import sys

from graphe import Graphe
from complete import *
from stable import *
from skep import *
from credul import *

''' Returns the list of all arguments and the list of attacks between arguments according to a file 'af_file' given in parameter '''
def read_file(af_file):
    liste_arg=[]
    liste_att=[]
    with open (af_file,"r") as my_file:
        lines = my_file.readlines()
        for l in lines :
            if (l.startswith("arg(")):
                liste_arg.append(l[4])
            if (l.startswith("att(")):
                liste_att.append((l[4], l[6]))       
        return liste_arg, liste_att

arguments, atk = read_file(os.path.join(os.getcwd(), "..", "dossier_test", sys.argv[4])) #TODO: prendre que argv[4] pr rendu final

g = Graphe(arguments,atk)

''' Calls the corresponding function based on the command arguments '''
def arg_switch(value, arguments):
    match value:
        case "VE-CO":
            return VE_CO(g, arguments)
        case "DC-CO":
            return DC_CO(g, arguments)
        case "DS-CO":
            return DS_CO(g, arguments)
        case "VE-ST":
            return VE_ST(g, arguments)
        case "DC-ST":
            return DC_ST(g, arguments)
        case "DS-ST":
            return DS_ST(g, arguments)
        case _:
            return None
        
return_value =  arg_switch(sys.argv[2],  sys.argv[6])

if return_value:
    print("YES")
elif return_value == False:
    print("NO") 
else: 
    print("Error: unexpected argument")
    









# #print(complete(g))
# print(f"#sans conflit : {conflict_free_subsets(g)}")
# res = []
# for e in g.arguments:
#         res.append(defends(e, g))
# print(f"#defends : {res}")
# print(f"#admissibles : {admissibles(g)}")

# stable =stable(g)
# print(f"#stable : {stable}")
# print(f"#skep de stable: {skeptical(stable,g.arguments)}")
# print(f"#cred de stable: {credul(stable,g.arguments)}")

# #test fonction VE_ST verifiy if is stable
# sol_non_stable={'D','B'}
# print(f"#test VE_ST : {VE_ST(g,sol_non_stable)}")

# #test fonction DC_ST is arg is in cred(stable)
# arg='D'
# print(f"#test DC_ST : {DC_ST(g,arg)}")

# #test fonction DS_ST is arg in all stable
# print(f"#test DS_ST : {DS_ST(g,arg)}")




# ##  A TESTER  LORSQUE COMPLETE SERA FINIS ##
# #test fonction VE_CO verifiy if is stable
# sol_non_stable={'D','B'}
# print(f"#test VE_CO : {VE_CO(g,sol_non_stable)}")

# #test fonction DC_CO is arg is in cred(stable)
# arg='D'
# print(f"#test DC_CO : {DC_CO(g,arg)}")

# #test fonction DS_CO is arg in all stable
# print(f"#test DS_CO : {DS_CO(g,arg)}")
