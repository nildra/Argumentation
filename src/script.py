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

option_p = ""
option_f = ""
option_a = ""

def printHelp():
    print("\n####### HELP #######\n", 
          "-f : PATH/TO/FILE_TEST.txt\n", 
          "-p : 'VE-CO' or 'VE-ST' or 'DS-CO' or 'DC-CO' or 'DS-ST' or 'DC-CO'\n",
          "-a : 'ARG1,ARG2,...ARGN' or 'ARG' or '[]'\n",
          "=> See README.MD for more details \n")

if len(sys.argv) != 7:
    print("Missing options!")
    printHelp()
    exit(1)

for i in range(len(sys.argv)):
    if sys.argv[i] == "-a":
        option_a = sys.argv[i+1]
    elif sys.argv[i] == "-p":
        option_p = sys.argv[i+1]
    elif sys.argv[i] == "-f":
        option_f = sys.argv[i+1]

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

arguments, atk = read_file(option_f)
#arguments, atk = read_file(os.path.join(os.getcwd(), "..", "dossier_test", option_f)) #only option_f for final version

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
        
return_value =  arg_switch(option_p,  option_a.upper())

if return_value:
    print("YES")
elif return_value == False:
    print("NO") 
else: 
    print("Error: unexpected argument")
