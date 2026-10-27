def doble_print(tall):
    print(tall * 2)

def doble_return(tall):
    return tall * 2
    print("Ferdig!")
doble_print(5)
doble_return(5)
a = doble_print(5)
b = doble_return(5)

print(a)
print(b)
print(doble_return(5) + 1)
#print(doble_print(5) + 1)  # (Denne vil gi en feilmelding!)
print(doble_return(doble_return(3)))
# Funksjonen som bare regner ut og returnerer arealet
def regn_areal(lengde, bredde):
    return lengde * bredde

# Prosedyren som bruker funksjonen til å skrive ut svaret pent
def skriv_areal(lengde, bredde):
    areal = regn_areal(lengde, bredde)
    print(f"Arealet er {areal}")

skriv_areal(5, 4)
#Hvorfor ble ingenting skrevet ut fra doble_return(5) i steg 2? fordi return lagrer bare svarer den viser ikke i terminalen i motsetning til print som viser men ikke lagrer. man kan ikke regne videre på print forhold til return
#2. Hva var a i steg 3? Hva tror du denne verdien betyr? når man plusser på print så blir det å plusse på ingenting for python fordi svaret ikke blir lagret. naturligvis viser none i terminalen.
#3. Hva sier steg 6 om hva return gjør? vi la til print i funksjonen men return er en linej over. mtp at return får funksjonen til å stoppe og lagre variablen skjer ingenting selv om vi skrev print.
#4. Forklar forskjellen på en prosedyre og en funksjon med egne ord. Når ville du valgt den ene, og når den andre?
#en prosedyre utfører en handling uten å gjøre noe lagring eller gir ingen svar tilbake
#en funksjon derimot regner ut en verdi og gir noe tilbake som vi kan lagre "areal" "return"
#Når velger man hva? Vi velger en funksjon når vi trenger resultatet for å regne videre på det i koden. Vi velger en prosedyre når vi bare vil vise en ferdig handling eller skrive ut tekst på skjermen.