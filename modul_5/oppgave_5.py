def lag_hilsen():
    melding = "Hei!"
    print(melding)

lag_hilsen()
#print(melding)

by = "Bryne"
def skriv_by():
    print(f"Jeg bor i {by}.")
skriv_by()



def doble(tall):
    tall = tall *2
    print(f"Inne: {tall}")
tall = 5
doble(tall)
print(f"ute: {tall}")





def legg_til_poeng(poeng: int) -> int:
    return poeng + 10

poeng = 0
poeng = legg_til_poeng(poeng)
print(poeng)


def legg_til_poeng(poeng: int, antall: int) -> int:
    return poeng + antall

def trekk_fra_poeng(poeng: int, antall: int) -> int:
    return poeng - antall

# Start med 0 poeng
poeng = 0

# Legg til 10, legg til 25, og trekk fra 5
poeng = legg_til_poeng(poeng, 10)
poeng = legg_til_poeng(poeng, 25)
poeng = trekk_fra_poeng(poeng, 5)

print(f"Sluttpoengsum: {poeng}")

#1. I snutt 1 og 3 er variablene inne i funksjonen atskilt fra resten av programmet. Forklar med egne ord hva som skjedde i hver av dem.
#Variabelen medling var bare lagret lokalt inni i funksjonen så da vi prøvde og kjøre denne utenofr kjræsjet det
# variabelen tall ble endret inni i funksjonen men det påvirket ikke utenfor funksjonen som er naturlig etter snutt 1


#2. I snutt 2 kunne funksjonen lese by, men i del 2 kunne den ikke endre poeng. Hva tror du er forskjellen?
#fordi når noe lagres globalt kan også lokale funksjoner bruke men ikke motsatt.
#python lar deg lese globale funksjoner men du får ikke endret den fordi det kan lage rot i systemet om man har mulighet til å endre lokalt

#3. Løsning A og B virker begge. Hvilken ville du valgt? Tenk deg et program med 20 funksjoner der alle kan endre poeng med global. Hva skjer når poengsummen plutselig blir feil?
#hvis flere funksjoner kan endre på en global blir det vanskelig og finne ut hva som fikk det til å kræsje.
#med løsning b flyter data kontrollert inn og ut av funksjonene det gjør også koden enklere og forstå 
#fordi man beskriver hva man forventer av type data.






