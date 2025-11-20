#Variabel som skal lagre score basert på valg
score = 0 

#Farger rød, gul og grønn som skal vise hvor bra du gjorde det
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"

#importere os og definere funskjon for å fjerne tekst fra tidligere valg
#Dette skal hjelpe med brukervennlighet for å ikke ha mye tekst i terminalen på en gang
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Velkommen tekst
print ("Velkommen, du skal nå ta rollen som prosjektleder Erling.")
print ("Du vil bli presentert med tre konflikter, Prøv å ta gode valg")

#Teskt der bruker blir presentert for konflikt mellom Silje og Sivert
print ("Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt.")
print("Du skal nå velge mellom to alternativer.")
print ("Alternativ A: Du illustrerer dine meninger og individuellt sjekker deres oppfatning.")
print ("Alternativ B: Du involverer HR")
#Variabel Valg1 der man kan velge mellom A og B og poengscore
Valg1 = input ("Velg alternativ A eller B").upper()
if Valg1 == "A":
    score += 1

else:
    score -= 1

clear_screen()

#Tekst der bruker blir presentert for konflikt mellom Jabir og Hamdi
print ("Konflikt: De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print ("Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print("Du skal nå velge mellom to alternativer.")
print("Alternativ A: Du holder et møte med fokus på krav, risiko og en klart beslutning.")
print("Alternativ B: Du lar Jabir og Hamdi finne ut av det selv")
#Variabel Valg2 der man kan velge mellom A og B
Valg2 = input ("Velg alternativ A eller B").upper()
if Valg2 == "A":
    score += 1
else:
    score -= 1

clear_screen()
#Tekst der bruker blir presentert for hvordan han skal motivere teamet
print("Hvordan skal du motivere teamet ditt)")
print("Alternativ A: Du tar tid til sosial aktivitet der teammedlemmer kan diskutere hva som fungerer og ikke fungerer.")
print("Alternativ B: Du setter ikke av tid til samarbeid, men pusher mot leveranse.")
#Variabel Valg3 der man kan velge mellom A og B
Valg3 = input ("Velg aternativ A eller B").upper()
if Valg3 == "A":
    score += 1
else:
    score -= 1
clear_screen()
#Endepunkter basert på tidligere valg
if score == 3:
    print(GREEN + "Du viser til høy problemløsningsevne og evne til å motivere teamet ditt!")
elif score == 2 or score == 1:
    print(YELLOW + "Du viser til middels problemløsningsevne og sliter med å motivere teamet ditt")
else:
    print(RED + "Du viser til lav problemløsningsevne og evner ikke til å motivere teamet ditt")
    





