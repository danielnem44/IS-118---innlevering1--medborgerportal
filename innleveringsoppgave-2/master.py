# master.py
# Interaktiv historie for innlevering IS-118, basert på Del 1 (Erling og medborgerportalen).
# Programmet inneholder tre beslutningspunkter med tilhørende valg og tre mulige utfall.
# Dette er gruppens felles versjon, samlet og kvalitetssikret etter individuelle bidrag.

#"-------------------------------------------------------------------"

#I denne delen er et program som har to valfunkjsoner, med 3 beslutninger.
#Først lager en definisjon for valgmulihetene og begrenser den slik at hvis brukeren
#skriver inn noe annet enn de gitte alternativene, så får de beskjed om å prøve igjen.

def valg(test):
    #Denne funksjonen sjekker om valget er gyldig
    while True:
        print()
        svar = input(test).strip()
        if svar == "1" or svar == "2":
            return svar
        print("Ugyldig valg, prøv igjen.")

#Velger å lage en intro for brukeren slik at de forstår hva som er grunnlaget:
def intro():
    print("--------------------------------")
    print("Erling og beslutningene som prosjektleder")
    print("--------------------------------")
    print()
    print("Erling er prosjektleder for digital medborgerportal.")
    print("Teamet består av utviklere, designere og folk fra kommunen.")
    print("Det er mye press og usikkerhet i gruppa.")
    print()
    print("Noen er uenige om funksjoner, andre om prioriteringer.")
    print("---------------------------------")
    print()

#i NEste delen må lage selve valgene som brukeren skal ta.
#Her vil brukeren bli presentert for en situasjon og to valg.
#Brukeren må så velge ett av de to alternativene.
#Hver funksjon returnerer valget som brukeren gjør.
#Beslutning 1
def avgjørelse1():
    print("Beslutning 1:")
    print("Hvordan vil du håndtere uenigheten i teamet?")
    print("Silje vil ha fancy funksjoner og innovasjon.\nMen Sivert vil heller fokusere på det grunnleggende og enkleste.")
    print("----------------------------------")
    print("Hvordan kan dette løses?")
    print("1: Ha en individuell samtale med begge for å forstå deres perspektiver.")
    print("2: Involvere HR da de har et bedre grunnlag for å håndtere konflikter.")
    Første_valg = valg("Skriv inn 1 eller 2 for å velge: ")
    return Første_valg

#Samme oppsett for den andre beslutningen:
#Her vil brukeren bli presentert for en situasjon og to valg.
#Brukeren må så velge ett av de to alternativene.
#Hver funksjon returnerer valget som brukeren gjør.
#Beslutning 2
def avgjørelse2():
    print("Beslutning 2:")
    print("Hamdi ønsker faste og regelmessige møter for å holde alle oppdatert.")
    print("Jabir vil heller ha uformell dialog, og korte oppdateringer.")
    print("----------------------------------")
    print("Hvordan kan dette løses?")
    print("1: Foreslå en hybrid tilnærming med både faste møter og uformelle oppdateringer.")
    print("2: La teamet bestemme hva de foretrekker.")
    Andre_valg = valg("Skriv inn 1 eller 2 for å velge: ")
    return Andre_valg

#I den avgjørelsen vil brukeren bli presentert for en situasjon og to valg.
#Brukeren må så velge ett av de to alternativene.
#Hver funksjon returnerer valget som brukeren gjør.
# Beslutning 3
def avgjørelse3():
    print("Beslutning 3:")
    print("Teamet viser preg av innsatsen og er slitne.")
    print("Som nevnt i oppgaven, er det 3 uker igjen til fristen.")
    print("----------------------------------")
    print("Hvordan kan dette løses?")
    print("1: Arranger en revy for å lette stemningen og motivere teamet, samt fange innspill.")
    print("2: Øk tempoet og sett klare mål for de siste ukene.")
    Tredje_valg = valg("Skriv inn 1 eller 2 for å velge: ")
    return Tredje_valg

#Videre etter som avgjørelsene er definert, må vi definere utfallene basert på valgene brukeren gjør.
#Hver funksjon vil ta inn valgene som argumenter og gi en tilbakemelding basert på kombinasjonen av valg.
#Beregner utfall basert på valg
def beregn(valg1, valg2, valg3):
    if valg1 == "1" and valg2 == "1" and valg3 == "1":
        print("Utmerket! Du har håndtert konflikter og motivert teamet på en effektiv måte.")
    elif valg1 == "2" and valg2 == "2" and valg3 == "2":
        print("Dessverre, dette førte til mer misnøye i teamet og dårligere resultater.")
    else:
        print("Dine beslutninger hadde både positive og negative konsekvenser for teamet.")

#Hovedprogram
def main():
    intro()
    valg1 = avgjørelse1()
    valg2 = avgjørelse2()
    valg3 = avgjørelse3()
    beregn(valg1, valg2, valg3)

    print("Valgene er tatt og utfallet er beregnet. Takk for deltagelsen!")

if __name__ == "__main__":
    main()