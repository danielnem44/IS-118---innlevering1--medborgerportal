# nemeye.py
# Min versjon av Erling historie :)

def les_valg(test):
# Funskjon for å lese 1 eller 2
    while True:
        print()
        svar = input(test).strip()
        if svar == "1" or svar == "2":
            return svar
        print("Ugyldig valg. Du må skrive 1 eller 2.")
# her begynner historien selve historien min.
# intro funksjon viser litt teskt om Erling, teamet og storming-fase.
def intro ():
    print("----")
    print("Erling og Medborgerportalen")
    print("----")
    print()

    print("Erling er prosjektleder for digital medborgerportal.")
    print ("Team har utviklere, designere og folk fra kommune.")
    print ("Nå er det mye friksjon og stress i teamet.")
    print ()

    print("Silje og Sivert krangler om løsning.")
    print ("Hamdi og Jabir er uenige om digital folkemøter.")
    print ("Prototypen skal levers om tre uker, alle kjenne press.")
    print ()

    print("Dette ligner storming-fase i gruppe:")
    print("- mer konflikt")
    print("- litt personlige følelse")
    print("- usikkerhet om mål og struktur")
    print()

    print("Du er Erling nå. Du må velge hva du gjøre i tre situasjon.")
    print ("Valgene dine gir forskjellig slutt på historien.")
    print()

# Denne function er for første valg i historien.
# Det handler om konflikt mellom Silje og Sivert.
# Prøver viser to valg som Erling kan gjøre, enten snakke med dem, eller bruke HR. Bruker må velge 1 eller 2. 

def beslutning_1():
    print("\n--- Beslutning 1: Silje og Sivert krangler ---\n")
    print("Silje vl mer innovasjon og frihet i design.")
    print ("Sivert vil ha trygg løsning, billig og ikke for crazy.")
    print ("Konflikt har gåt litt fra sak til person.")
    print()

    print("Hva gjør du som Erling?")
    print("1) Ta individuelle samtale med begger (1A).")
    print (" Du bruker enkel dialog, HES-modell og prøver forså dem.")
    print("2) Involvere HR (1B)")
    print(" Du ber HR om hjelp som nøytral part.")

# Bruker må skrive 1 eller 2, og funksjon les_valg sjekke det for meg
#Så returnere jeg valget så jeg kan bruker det senere i historien. 

    valge1 = les_valg("skriv 1 eller 2 for beslutning 1: ")
    return valge1

# Denne function er for andre valg i historien.
# handler om Hamdi og Jabir som er uenige om  folkemøter.
# Prøver viser to valg som Erling kan gjøre, enten snakke med dem sammen, eller bare vente. begge valg kan gi forskjellig konsekvens.

def beslutning_2():
    print("\n--- Beslutning 2: Hamdi og Jabir krangler ---\n")
    print("Hamdi vil bruke kommunens eksisterende plattform for folkemøter.")
    print("Jabir vil ha mer åpen løsning med fri dialog.")
    print("Uenighet er ikke eksplosijon enda, men den ulmer litt.")
    print()

    print("hva gjør du som Erling?")
    print ("1) Ha felles møte med Hamdi og Jabir (2A).")
    print (" Du snakker om krav, risiko og prøver tar klar beslutning.")
    print ("2) Avvente og håpe de ordne selv (2B).")
    print(" Du sparer tid nå, mem risiko for mer konflikt senere.")

    valge2 = les_valg("skrive 1 eller 2 for beslutning 2:")
    return valge2

#Dette e 3 og siste valg , her er fokus  på motivasjon i teamet.
#Erling må velge enten sosial aktivitet (3A) eller presse på leveranse (3B)
#dette valget påvirker slutten ganske mye.

def beslutning_3():
    print("\n--- Beslutning 3: Motivasjon i teamet ---\n")
    print ("Teamet ser sliten ut. Lav energi.")
    print ("Konflikter blir ikke snakka om, men de er ikke borte.")
    print("Tre uker igjen til prototype ska leveres.")
    print()

    print ("Hva gjør du som Erling?")
    print("1) Kort 'revy' / retro + litt sosial aktivitet (3A).")
    print(" Alle sier hva funker bra og dårlig. Du gjør regler for")
    print(" Komunikasjon lit tydeligere og har litt sosialt på slutten.")
    print("2) Presse hardt mot leveranse (3B).")
    print(" Du deler ut konkrete oppgaver med korte frister.")
    print(" Ingen tid satt av til å snakke om samarbeid. ")

    valge3 = les_valg("Skriv 1 eller 2 for beslutning 3: ")
    return valge3

# Dette e  beste utfall i historien, here har Erling tatt gode og fokusert på både konflikt og motivasjon.
#Teamet får bedre samarbeid og prototype blir levert bra.

def utfall_best():
    print ("\n--- Utfall 1: Tillit bygges og samarbeid blir bedre ---\n")
    print ("Du tok tak i konflikt (for eksempel ved å snakke med folk og eller ha møte),")
    print("og du valgte også å bruke tid på trygghet og sosial aktivitet (3A).")
    print()

    print("Teamet forstår hverandre litt bedre nå.")
    print ("Konfliktnivå går ned, og folk tør snakker mer ærlig.")
    print ("Prototype blir levert, og gruppa beveger seg mot norming-fase.")
    print ("Motivasjon og tillit er sterkere enn før.")

#Dette er mellom-utfall, ikke bra og ikke dårlig . noen problemer ble løst, men ikke alt. teamet funke ok, men motivasjon er ustabil.
#prototype blir levert, men samarbeidet er litt sårbart.

def utfall_midt():
    print ("\n---- Utfall 2: Leveranse, men motivajson er ustabil ----\n")
    print ("Noen problemer bler løst, men ikke alle.")
    print ("Du har kanskje tatt et bra valg og et mindre bra, eller presser mer ")
    print("på leveranse enn på relasjoner.")
    print()

    print("prototype blir levert, men samarbeidet er litt sårbart.")
    print("Noen i teamet føler seg fortsatt ikke helt hørt.")
    print("Motivasjon går opp og ned, og gamle konflikter kan komme tilbake senere.")

#dette e dårligste utfall. Erling har unngått konflikt og bare pressa på levering.
#teamet blir frustrert, prototype blir forsinka og relasjoner blir dårlige.
def utfall_worst():
    print("\n--- Utfall 3: Forsinket prosjekt og dårlige relasjoner---\n")
    print ("Du har stort sett ikke tatt tak i konflikter (1B + 2B),")
    print(" og du valget bare å presse på leveranse (3B).")
    print()

    print("Teamet blir mer frustrert. Misnøye går inn i stillhet.")
    print("Prototype blir forsinket, eller veldig dårlig kvalitet.")
    print("Tillit mellom folk i teammet svekkes mye, og prosjektet trenger nesten restart.")

#Bruker tre tekstbaserte valge og bestemmer slutt
#Har tatt minst ett aktivt konflikt valg og motivasjonstiltak
#Har unngått konflikt hele veien og bare pressa på levering
#Alle andre kombinasjin går til midten. 
def beregn_utfall(valg1, valg2, valg3):
    if valg3 =="1" and (valg1=="1" or valg2=="1"):
        utfall_best()
    elif valg3=="2" and valg1=="2" and valg2=="2":
        utfall_worst()
    else:
        utfall_midt()


#denne funksjon er bare liten oppsummering. Jeg prøver forklare kort hva storming-fase betyr, og hvordan valgene brukeren tok påvirke slutten.
def refleksjon():
    print("\n---- kort refleksjon ----\n")
    print("Storming-fase betyr ikke at gruppa er ødelagt.")
    print("Det er naturlig del når folk har ulike perspektiv og vil noe annet.")
    print("Men hvis leder ikke tar tak, kan grupp bli stående fast i stormen.")
    print()

    print("Her så du hvordan valg om konflikt, møter og motivajson gir forskjellig slutt.")
    print ("Små valg fra Erling kan avgjøre om team går videre til norming eller ikke.")

# dette er hoved funsjonen som kjøre alt. Først kommer intro, så tre valg, så beregner jeg utfall. 
#Helt til slutt viser jeg refleksjon og en liten takk tekst. 
def main():
    intro()
    valg1=beslutning_1()
    valg2=beslutning_2()
    valg3=beslutning_3()

    beregn_utfall(valg1, valg2, valg3)
    refleksjon()
    print()

    print("Takk skal du ha, for at du spilte min versjon.")
    
if __name__=="__main__":
    main()
    

    



    





     
    