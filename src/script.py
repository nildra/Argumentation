## Script principal 

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
        #print((liste_att, liste_arg)) 
        return liste_arg, liste_att

def test():

    args, atk = read_file("/Users/rafika/Argumentation/dossier_test/test_af1.apx")
    print(args, atk)

test()