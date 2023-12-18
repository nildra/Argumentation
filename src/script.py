#
# Main file
#

import os
import sys

from graphe import Graphe
from extension import *

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


arguments, atk = read_file(os.path.join(os.getcwd(), "..", "dossier_test", sys.argv[1])) #commande pr exec : "python3 script.py fichierTest.apx"
#print(os.path.join(os.getcwd(), "..", "dossier_test", "test_af1.apx"))
#print(arguments, atk)

g = Graphe(arguments,atk)
#print(complete(g))
#print(find_conflict_free_subsets(g))

print(admissibles(g))