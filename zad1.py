l=list(range(1,11))
import random
n_l=[]
while len(l)>=2:
    a=random.choice(l)
    l.remove(a)
    b=random.choice(l)
    l.remove(b)
    n_l.append((a,b))
print(n_l)