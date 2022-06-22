# 2. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na broevi vo lista, vo druga lista da se zacuvaat elementite kvadrirani

numberOfInput = int(input("Kolku broevi sakate da vnesite: "))
lista = []
kvadrirani = []

for i in range(0, numberOfInput):
    temp = int(input("Vnesete broj: "))
    lista.append(temp)
    kvadrirani.append(temp*temp)

print(lista, kvadrirani)