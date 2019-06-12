def funkcija_map(y): #kvadrira elemente
    return y**2

def funkcija_filter(y): #vraca prirodne brojeve
    if y>=0:
        return True
    else:
        return False

def funkcija_reduce(x,y): #sumira
    return x+y

def MAPP(funk, iterab): #realizovana MAP funkcija
    for x in range (0, len(iterab)):
        iterab[x] = funk(iterab[x])
    return iterab

def FILTERR(funk, iterab): #realizovana FILTER funkcija
    new_iterab=[]
    for x in range (0, len(iterab)):
        if funk(iterab[x]) == True:
            new_iterab.append(iterab[x])
        else:
            continue
    return new_iterab

def REDUCEE(funk, iterab):  #realizovana REDUCE funkcija
    y = iterab[0]
    for x in iterab[1:]:
        y = funk(y, x)
    return y

lista = [1,2,3,4,5]
filter_final = FILTERR(funkcija_filter, lista)
print(filter_final)
map_final = MAPP(funkcija_map, lista)
print(map_final)
reduce_final = REDUCEE(funkcija_reduce, lista)
print(reduce_final)