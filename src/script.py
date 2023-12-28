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

''' Returns the list of all arguments and the list of attacks between arguments according to a file given in parameter '''
def read_file(name):
    liste_arg=[]
    liste_att=[]
    with open (name,"r") as my_file:
        lines = my_file.readlines()
        for l in lines :
            if (l.startswith("arg(")):
                liste_arg.append(l[4])
            if (l.startswith("att(")):
                liste_att.append((l[4], l[6]))       
        return liste_arg, liste_att

arguments, atk = read_file(os.path.join(os.getcwd(), "..", "dossier_test", sys.argv[1]))
#print(os.path.join(os.getcwd(), "..", "dossier_test", "test_af1.apx"))
#print(arguments, atk)

g = Graphe(arguments,atk)

#print(complete(g))
print(f"#sans conflit : {conflict_free_subsets(g)}")
res = []
for e in g.arguments:
        res.append(defends(e, g))
print(f"#defends : {res}")
print(f"#admissibles : {admissibles(g)}")

stable =stable(g)
print(f"#stable : {stable}")
print(f"#skep de stable: {skeptical(stable,g.arguments)}")
print(f"#cred de stable: {credul(stable,g.arguments)}")

#test fonction VE_ST verifiy if is stable
sol_non_stable={'D','B'}
print(f"#test VE_ST : {VE_ST(g,sol_non_stable)}")

#test fonction DC_ST is arg is in cred(stable)
arg='D'
print(f"#test DC_ST : {DC_ST(g,arg)}")

#test fonction DS_ST is arg in all stable
print(f"#test DS_ST : {DS_ST(g,arg)}")




##  A TESTER  LORSQUE COMPLETE SERA FINIS ##
#test fonction VE_CO verifiy if is stable
sol_non_stable={'D','B'}
print(f"#test VE_CO : {VE_CO(g,sol_non_stable)}")

#test fonction DC_CO is arg is in cred(stable)
arg='D'
print(f"#test DC_CO : {DC_CO(g,arg)}")

#test fonction DS_CO is arg in all stable
print(f"#test DS_CO : {DS_CO(g,arg)}")
