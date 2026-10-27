def finn_karakter(poeng: int) -> str:
    if poeng >= 90:
        return "A"
    if poeng >= 80:
        return "B"
    if poeng >= 70:
        return "C"
    if poeng >= 60:
        return "D"
    else:
        return "F"

def skriv_resultat(navn: str, karakter: str) -> None:
    print(f"Hei {navn}! Din karakter er: {karakter}")

brukerens_navn = input("Hva heter du? ")
brukerens_poeng = int(input("Hvor mange poeng fikk du? "))
def doble(tall: int) -> int:
    return tall * 2

# Prøv å kalle den med en tekst-streng i stedet for et tall:
print(doble("5"))

# 1. Vi bruker funksjonen til å finne karakteren og lagrer den i en variabel
min_karakter = finn_karakter(brukerens_poeng)

# 2. Vi sender navnet og karakteren inn i prosedyren for å skrive det ut
skriv_resultat(brukerens_navn, min_karakter)





