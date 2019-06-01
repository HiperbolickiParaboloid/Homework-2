def bs_single(string):
    list = string.split(' ')
    rjecnik = {"quote": list[0], "quantity": int(list[1]), "price": float(list[2]), "status": list[3].lower()}
    if rjecnik["status"]=='b':
        B=str(rjecnik["quantity"]*rjecnik["price"])
        S=str(0)
    else:
        S=str(rjecnik["quantity"]*rjecnik["price"])
        B=str(0)
    return 'Buy:'+B+' Sell:'+S

def bs_multiple(string):
    B=0
    S=0
    list=string.split(',')
    for x in list:
        list1=x.split(' ')
        rjecnik = {"quote": list1[0], "quantity": int(list1[1]), "price": float(list1[2]), "status": list1[3].lower()}
        #print (rjecnik)
        if rjecnik["status"]=='b':
            B=B+(rjecnik["quantity"]*rjecnik["price"])
            S=S+0
        else:
            S=S+(rjecnik["quantity"]*rjecnik["price"])
            B=B+0
    B2 = round(B,2)
    S2 = round(S,2)
    B1 = str(B2)
    S1 = str(S2)
    return 'Buy:'+B1+' Sell:'+S1

unos = "GOOG 300 542.0 B" 
unos = "ZNG 1300 2.66 B,CH15.NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"
if unos.count(',') == 0:
    print(bs_single(unos))
else:
    print(bs_multiple(unos))




