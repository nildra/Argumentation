def skeptical(solutions,arguments):
    result=[]
    for arg in arguments:
        if all(arg in solution for solution in solutions ):
            result.append(arg)
    return result

print(skeptical([['B','D'],['A','D']],['A','B','C','D','E']))