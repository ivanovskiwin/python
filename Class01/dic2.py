# . Da se kreira prazen dictionary, korisnikot da moze da vnese ime, prezime, mesto na ziveenje, mail i telefonski broj. Da se ispecati toj dictionary(pregledno) i da mu se dade opcija na korisnikot da izbirese nekoj key od mail ili telefonski broj, ako izbere drug da se ispecati deka ne e dostapna taa operacija
dictionary = {}

dictionary['ime'] = input("Vnesete ime: ")
dictionary['prezime'] = input("Vnesete prezime: ")
dictionary['telbroj'] = input("Vnesete telefonski broj: ")
dictionary['mesto na ziveenje'] = input("Vnesete mesto na ziveenje: ")
dictionary['mail'] = input("Vnesete mail: ")

for key, value in dictionary.items():
    print("{key} : {value}".format(key=key, value=value))

choice = input("Vnesete sto sakate da izbrisete. telbroj ili mail:  ")

if choice=="telbroj":
    dictionary.pop("telbroj")
elif choice=="mail":
    dictionary.pop("mail")
else:
    print("Taa opcija ne e vozmozna.")

print(dictionary)