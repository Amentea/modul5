
def regn_pris(antall, pris_per_stk):
    total = antall * pris_per_stk
    return total

def skriv_kvittering(navn, total):
    print(f"Kvittering for: {navn}")
    print(f"Totalt: {total} kr")

def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
skriv_kvittering("Michael", pris)
print(f"Du betalte: {pris} kr.")
avslutt()

#1. Hva var feilene? Beskriv dem kort med egne ord.
Syntaks feil og manglet blant annet kolon og inrykk på øverste.
#Den ene funksjonen manglet return

#2. Hvilke to feil ga ingen feilmelding? Hvordan oppdaget du dem?
# funksjonen regn_pris manglet return total, og at avslutt ble kalt uten parenteser. Python krasjet ikke av den grunn, men vi oppdaget det fordi programmet ikke returnerte prisen (den ble None), og avslutningsmeldingen ble aldri skrevet ut på skjermen fordi funksjonen aldri ble faktisk kjørt uten parenteser.

#. Hvordan rettet du linjen med {total}? Hvorfor fungerte ikke den opprinnelige linjen?
fordi den opprinnelige linen var total som var lagret lokalt hovudprogrammet kjente kun til pris

print(avslutt)