def funkcija_map(y): #kvadrira elemente
    return y**2

def funkcija_filter(y): #vraca prirodne brojeve
    if y>=0:
        return True
    else:
        return False

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

filter_lista = (-2,4,0,6,-7,8)
nova_lista_filter = FILTERR(funkcija_filter, filter_lista)
print(nova_lista_filter)
lista = [1,2,3,4,5]
nova_lista = MAPP(funkcija_map, lista)
print(nova_lista)