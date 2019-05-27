vrata = [False for x in range(1,6)]
#def zatvori_otvori_vrata(lista):
  #  promijenjena_vrata=[not x for x in lista if ((lista.index(x)+1)%x)==0]
   # return(promijenjena_vrata)
neg = lambda a : not a
for y in range(1,6):
    for x in vrata:
        if ((vrata.index(x)+1)%y)==0:
            vrata[x] = not vrata[x]
print(vrata)   
#c=map(neg,vrata)
#print(list(c))