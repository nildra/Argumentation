def credul(solutions, arguments):
    result =[]
    for arg in arguments:
        for sol in solutions :
            if (arg in sol) and (not (arg in result)):
                result.append(arg)
                break

    return result


print(credul([['B','D'],['A','D']],['A','B','C','D','E']))