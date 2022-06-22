# 3. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na broevi, i vo razlicni listi da se sortiraat broevite pomali od 10, pomali od 100, pomali od 1000 i pogolemi od 1000. Da se ispecata site listi

numberOfInput = int(input("Kolku broevi sakate da vnesite: "))
listaDesetki = []
listaStotki = []
listaDoIljada = []
listaPogolemiOdIljada = []
for i in range(0, numberOfInput):
    temp = int(input("Vnesete broj: "))
    if temp<=10:
        listaDesetki.append(temp)
    elif temp>10 and temp<=100:
        listaStotki.append(temp)
    elif temp>100 and temp<=1000:
        listaDoIljada.append(temp)
    elif temp>1000:
        listaPogolemiOdIljada.append(temp)

print(listaDesetki, listaStotki, listaDoIljada, listaPogolemiOdIljada)