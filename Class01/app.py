# Da se napravi programa vo koja korisnikot ke moze da vnese 10 elementi vo lista i da se ispecatti sekoj vtor element od 3tiot index do krajot

lista = []
for i in range(0, 10):
    temp = int(input("Vnesete broj"))
    lista.append(temp)

print(lista[3::2])

