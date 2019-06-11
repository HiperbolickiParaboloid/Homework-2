zanrovi = ['action','simulation','sports','fantasy','adventure']

def provjera_imena(ime): #provjera da li je uneseno ime igre ispravno
    if len(ime) <= 2 or len(ime) >= 50:
        return False
    else:
        return True

def provjera_ocjene(ocjena_unos): #provjerava da li je unesena ocjena ispravna
    if ocjena_unos.count('.')>1:
        return False
    for x in ocjena_unos:
        m = (x == '.' or x.isdigit())
        if m == False:
            return False
            break
    ocjena = float(ocjena_unos)
    round (ocjena,2)
    if ocjena <= 1 or ocjena > 10:
        return False
    else:
        return True

def provjera_godine(godina_unos): #provjerava ispravnost unosa godine
    if godina_unos.isdigit() == False:
        return False
    godina = int(godina_unos)
    if godina <=1950 or godina >=2019:
        return False
    else:
        return True

def provjera_izdavaca(izdavac): #provjerava da li je ispravno unesen izdavac
    if len(izdavac) <= 2 or len(izdavac) >= 40:
        return False
    else:
        return True

def provjera_zanra(zanr):
    zanr.lower()
    brojac = 0
    for x in zanrovi:
        if zanr == x:
            brojac = brojac +1
    if brojac > 0:
        return True
    else:
        return False

def unos_igrice():
    while 1:
        print('Molimo vas unesite ime igre:')
        ime_igrice = input()
        if provjera_imena(ime_igrice) == False:
            print('Nepravilan unos!')
        else:
            break
    while 1:
        print('Molimo vas unesite ocjenu igre:')
        ocjena_igre = input()
        if provjera_ocjene(ocjena_igre) == False:
            print('Nepravilan unos! Morate pravilno unijeti broj!')
        else:
            break
    while 1:
        print('Molimo vas unesite godinu izdavanja igre:')
        godina_igre = input()
        if provjera_godine(godina_igre) == False:
            print('Nepravilan unos! Morate pravilno unijeti godinu najranije 1950.!')
        else:
            break
    while 1:
        print('Molimo vas unesite ime izdavaca igre:')
        ime_izdavaca = input()
        if provjera_izdavaca(ime_izdavaca) == False:
            print('Nepravilan unos!')
        else:
            break
    while 1:
        print('Molimo vas odaberite neke od zanrova: action, simulation, sports, fantasy, adventure. Ako ih unosite vise, koristite dugme SPACE da ih razdvojite!')
        ime_zanra = input()
        lista_imena_zanrova = ime_zanra.split(' ')
        counter = 0
        for x in lista_imena_zanrova:
            if provjera_zanra(x) == False:
                print('Nepravilan unos zanra!')
                break
            else:
                counter = counter +1
        if counter == len(lista_imena_zanrova):
            break
    novi_red = ime_igrice+';'+ocjena_igre+';'+godina_igre+';'+ime_izdavaca+';'+ime_zanra+';'
    return novi_red   

def provjera_igrice(lista):
    sign = True
    if len(lista[0]) <= 2 or len(lista[0]) >= 50:
        return not sign
    ocjena = float(lista[1])
    round(ocjena, 2)
    if ocjena <= 1 or ocjena >= 10:
        return not sign
    godina = int(lista[2])
    if godina <=1950 or godina >=2019:
        return not sign
    if len(lista[3]) <= 2 or len(lista[3]) >= 40:
        return not sign
    mali_zanr = lista[4].lower() #pretvaranje svih karaktera 5og elementa liste u mala slova
    zanr = mali_zanr.split(' ') #splitovanje 5og elementa liste na osnovu white space-a
    presjek = (set(zanr) & set(zanrovi)) #trazenje zajednickih elemenata izmedju 5og elementa liste i liste zanrova
    lista_presjek = list(presjek) #konverzija presjeka u tip podatka LIST
    if (len(lista_presjek)) != (len(zanr)):
        return not sign
    return sign

f = open("./igrice.txt")
for line in f:
    lista = line.split(';')
    lista.pop()
    if provjera_igrice(lista) == True:
        print(line)
f.close()

fajl = open("./igrice.txt", "a")
while 1:
    print('Ako zelite da unesete jos neku igru ukucajte Da i pritisnite enter, a ako ne zelite ukucajte Ne i pritisnite enter:')
    y_n = input()
    da_ne = y_n.lower()
    if da_ne == 'da':
        x =unos_igrice()
        fajl.write('\n')
        fajl.write(x)
    elif da_ne == 'ne':
        break
    else:
        print("Nepravilan unos, molimo upisite Da ili Ne")
fajl.close()

fajl1 = open("./igrice.txt")
lista_igrica = []
for line in fajl1:
    l_game = line.split(';')
    rjecnik = {"naziv": l_game[0], "ocjena": float(l_game[1]), "godina": int(l_game[2]), "izdavac": l_game[3], "zanrovi": l_game[4].split(' ')}
    lista_igrica.append(rjecnik)
fajl1.close()

'''for x in lista_igrica:
    if x["godina"]>=2000:
        print (list(x.values()))'''

def filtriranje_po_nazivu(naziv):
    for x in lista_igrica:
        if x["naziv"].startswith(naziv):
            print (list(x.values()))

def filtriranje_po_ocjeni(ocjena):
    for x in lista_igrica:
        if x["ocjena"] >= ocjena:
            print (list(x.values()))

def filtriranje_po_godini_plus(godina):
    for x in lista_igrica:
        if x["godina"] >= godina:
            print (list(x.values()))

def filtriranje_po_godini_minus(godina):
    for x in lista_igrica:
        if x["godina"] <= godina:
            print (list(x.values()))

def filtriranje_po_izdavacu(izdavac):
    for x in lista_igrica:
        if x["izdavac"].startswith(izdavac):
            print (list(x.values()))

def filtriranje_po_zanru(zanrovi_za_filter):
    for x in lista_igrica:
        for y in x["zanrovi"]:
            if y in zanrovi_za_filter:
                print (list(x.values()))

print("\n")
brojevi_za_filtriranje = ['1','2','3','4','5']
filtriranje = [(1, "Filtriranje po nazivu."),(2, "Filtriranje po ocjeni."),(3, "Filtriranje po godinu."),(4, "Filtriranje po izdavacu."),(5, "Filtriranje po zanru.")]
print("Molimo vas da izaberete po cemu zelite da filtrirate igrice, i to unosom nekog od datih brojeva od 1 do 5.")
print(filtriranje)

while 1:
    filter_broj = input()
    if filter_broj not in brojevi_za_filtriranje:
        print("Molimo vas pravilno unesite broj.")
    else:
        break

if filter_broj == '1':
    print("Molimo unesite ime igre.")
    ime = input()
    filtriranje_po_nazivu(ime)
elif filter_broj == '2':
    print("Molimo unesite najnizu zeljenu ocjenu od 1 do 9.")
    ocjene = ['1','2','3','4','5','6','7','8','9']
    while 1:
        ocjena = input()
        if ocjena not in ocjene:
            print("Molimo vas pravilo unesite ocjenu.")
        else:
            break
    ocjena = float(ocjena)
    filtriranje_po_ocjeni(ocjena)
elif filter_broj == '3':
    print("Unesite zeljenu godinu.")
    godina = input()
    godina = float(godina)
    print("Ako zelite da vam prikazemo igre napravljene nakon unesene godine unesite +, a ako zelite da vam prikazemo igre napravljene prije unesene godine unesite -.")
    while 1:
        plus_minus = input()
        if plus_minus == '+':
            filtriranje_po_godini_plus(godina)
            break
        elif plus_minus == '-':
            filtriranje_po_godini_minus(godina)
            break
        else:
            print('Molimo unesite + ili -.')
elif filter_broj == '4':
    print("Molimo unesite ime izdavaca.")
    izdavac = input()
    filtriranje_po_izdavacu(izdavac)
elif filter_broj == '5':
    print("Molimo izaberite neki od ponudjenih zanrova: ", zanrovi, "Ako unosite vise zanrova, molimo vas ucinite to sa razmacima.")
    zanr = input()
    zanrovi_za_filter = zanr.split(' ')
    filtriranje_po_zanru(zanrovi_za_filter)
    
