# 1. Da se kreira prazen dictionary i korisnikot da moze da dodade 2 podatoci po negov izbor
dictionary = {}

for i in range(0,2):
    key = input("Vnesete key: ")
    value = input("Vnesete value: ")
    dictionary[key] = value

print(dictionary)