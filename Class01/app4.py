# 4. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, da se ispecati celata lista, da se prasa korisnikot dali saka da brise spored index ili spored vrednost, i korisnitkot da moze da izbrise eden element

numberOfInput = int(input("Kolku elementi sakate da vnesite: "))
lista = []
for i in range(0, numberOfInput):
    temp = input("Vnesete element: ")
    lista.append(temp)

print(lista)

choice = input("Dali sakate da brisete spored index ili spored vrednost. Vnesete soodvetno 1 ili 2: ")

if choice=="1":
    index = int(input("Vnesete index: "))
    lista.pop(index)
    print(lista)
elif choice=="2":
    removeQuery = input("Vnesete vrednost: ")
    lista.remove(removeQuery)
    print(lista)
else:
    print("Vnesete validen odgovor!")

