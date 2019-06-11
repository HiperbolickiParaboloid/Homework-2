def doors(n):
  vrata = []
  for x in range(1,n+1):
    jedna_vrata = [x,False]
    vrata.append(jedna_vrata)
  ucenici = list(range(1,n+1))
  for y in ucenici:
    for x in vrata:
      if x[0]%y == 0:
        x[1] = not x[1]
  br = 0
  for x in vrata:
    if x[1] == True:
      br = br + 1
  return br

v = doors(5)
print(v)