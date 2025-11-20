#Historie om Erling som Prosjektleder 
print("du skal ta valg for Erling som leder!")
print("du får tre besutninger som påvikrer laget")

#Besutning 1: Silje og Sivert 
valg1 = input("beslutning 1: konflikten mellom Silje og Sivert"
               "velg 'Samtaler' eller 'HR': ") 

#Besutning 2: Hamid og Jabir
valg2 = input("besutning 2: konflikiten mellom Hamid og Jabir"
            "velg 'møte' eller 'avente': ")

#Besutning 3: Motivasjon i laget 
valg3 = input("Beslutning 3: Laget er på felgen og virker slitne"
              "velg 'aktivitet' eller 'å levere': ")
#Her har vi tre besutninger med to mulige svar. basert på svarene man gir, får man ulike typer utfall. 
#grunnen for at jeg bruker "input" er for at man kan skrive svaret selv i terminal

Print:("RESULTAT")

#Hvordan det ender i forhold til det man har svart
if valg1 == "samtler" and valg2 == "møte" and valg3 == "aktivitet":
    print("Laget får mer tillit til hverandre og gå videre til Norming-fasen.")
    
elif valg3 == "leveranse":
    if valg1 == "HR" or valg2 == "avvente":
        print("Prototypen blir levert, men samarbeidet forblir svakt og motivasjonen i laget blir utsabil.")
    else:
        print("Prototypen blir levert, men motivasjonen synker drasisk")

else: 
    print("Konflikten løses delevis, men relasjonene er fortsatt svekket")
    #her er det forsjellelige utganger basert på på valgene man tar for Erling
    #grunnen for ar jeg bruker if, elif og else er for å lage forskjellige utganger og det gjør at pyhton velger utfallen basert på valgene du/erling har tatt 
    # har også valgt og bruke == som betyr Lik og jeg bruker den for å sjekke hva brukeren har skrevet inn i terminalen eksempel: valg3 == leveranse 
    #og om man da har skrevet leveranse så vil python gå til neste linje 
    # bruker print i if funksjonene for at python skal printe teksten i terminalen basset på de valgene man har tatt. 




