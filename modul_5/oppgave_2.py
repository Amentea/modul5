# 1. Funksjonen tar imot to parametere
def hilsen(navn, alder, by="Oslo"):
    print(f"Hei, {navn}! Du er {alder} år og bor i {by}")

# 2. Hvis du vil kalle den med faste navn, må du ha med både navn og alder:
hilsen("Miri", 25, "bryne")
hilsen("Einar", 30)
hilsen("Ironman", 26)

# 3. Hvis du vil bruke input fra brukeren, kan du gjøre det slik:
brukerens_navn = input("Hva heter du? ")
brukerens_alder = input("Hvor gammel er du? ")

# Husk å sende inn de nye variablene som argumenter!
hilsen(brukerens_navn, brukerens_alder)


hilsen(alder=31, navn="Michael")
#Forklar forskjellen på parameter og argument med egne ord. Pek ut hvilke ord i koden din som er hva. Parameter er ord som er satt som standard for eksempel by oslo. da kommer det til å stå det som deafult med mindre du argumenterer i koden som foreksempel bryne da. argument overstiger alltid parameter.
#  Ga steg 4 feilmelding? Hvorfor, eller hvorfor ikke? fordi python følger bare jobben slavisk. den skjønner ikke at den har gjort feil.
#I steg 2 het variabelen din noe annet enn parameteren. Fungerte det likevel? Hva sier det om sammenhengen mellom argument og parameter? jeg skjønte ikke denne så hoppet over
#Hvorfor fungerte steg 6 selv om rekkefølgen var snudd? Når tror du navngitte argumenter er nyttige?    fordi python bare gjør jobben sin slavisk den skjønner ikke at du har forvekslet. navgitte argument er essensielt der rekkefølgen på argumentene ikke kommer som forventet. 







