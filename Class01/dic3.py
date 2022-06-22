# 3. Da se kreira prazen dictionary vo koj korisnikot ke moze da gi vnese licnite podatoci za nekoj student (ime, prezime, fakultet, index) vo vgnezden dictionary da se vnesat otcenite so struktura predmet: otcena. Da se presmeta prosekot i da se zapise vo nov key

studenti = {}

ime = input("Vnesi ime: ")
studenti["ime"]=ime
prezime = input("Vnesi prezime: ")
studenti["prezime"]=prezime
fakultet = input("Vnesi fakultet: ")
studenti["fakultet"]=fakultet
index = input("Vnesi index: ")
studenti["index"] = index
brojNaPredmeti = int(input("Kolku predmeti sakate da vnesite: "))
studenti["ocenki"] = {}
for i in range(0, brojNaPredmeti):
    imeNaPredmet = input("Vnesi Ime na predmet: ")
    ocenkaNaPredmet = int(input("Vnesi Ocenka: "))
    studenti["ocenki"][imeNaPredmet]=ocenkaNaPredmet

average = 0
for ime, ocenka in studenti["ocenki"].items():
    average = average + ocenka

average = average/brojNaPredmeti

print(studenti)
print(average)