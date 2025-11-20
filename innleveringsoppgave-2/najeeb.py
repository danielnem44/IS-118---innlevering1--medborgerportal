# Interaktiv historie for del 2.
# Programmet bruker tre valg.
# Hvert valg lagres i en variabel.
# if, elif og else styrer historien.
# Koden kjøres i terminal.

print("Introduksjon:")
print("Du er Erling. Du leder et prosjektteam med konflikter.\n")

# Første valg
print("Beslutning 1: Konflikten mellom Silje og Sivert")
print(" 1) Private samtaler og megling")
print(" 2) Involvere HR for formell prosess")
choice1 = input("Velg 1 eller 2: ").strip()

# if-setning som skaper1
#  konsekvens
if choice1 == "1":
    desc1 = "Du bruker individuelle samtaler og får innsikt i situasjonen."
elif choice1 == "2":
    desc1 = "Du sender saken til HR og starter en formell prosess."
else:
    desc1 = "Valget er uklart. Konflikten forblir delvis uavklart."

print("\n" + desc1 + "\n")

# Andre valg
print("Beslutning 2: Uenigheten mellom Hamdi og Jabir")
print(" 1) Kort, strukturert fellesmøte")
print(" 2) Avvente og la dem løse det selv")
choice2 = input("Velg 1 eller 2: ").strip()

# if-setning for konsekvens
if choice2 == "1":
    desc2 = "Du leder et møte der begge får forklare sine syn."
elif choice2 == "2":
    desc2 = "Du lar dem prøve å finne en løsning uten direkte inngrep."
else:
    desc2 = "Valget er uklart. Uenigheten fortsetter."

print("\n" + desc2 + "\n")

# Tredje valg
print("Beslutning 3: Motivasjon i teamet")
print(" 1) Relasjonsbygging og retrospektiv")
print(" 2) Fremdrift og klare oppgaver")
choice3 = input("Velg 1 eller 2: ").strip()

# if-setning for konsekvens
if choice3 == "1":
    desc3 = "Du setter av tid til teamutvikling."
elif choice3 == "2":
    desc3 = "Du styrer stramt mot fremdrift."
else:
    desc3 = "Valget er uklart. Teamet får mindre retning."

print("\n" + desc3 + "\n")

# Lagre valg i trygge variabler
# Dette sikrer at sluttlogikken håndterer uklar input
valg1 = choice1 if choice1 in ("1", "2") else "u"
valg2 = choice2 if choice2 in ("1", "2") else "u"
valg3 = choice3 if choice3 in ("1", "2") else "u"

print("Avslutning:\n")

# Sluttutfall basert på kombinasjoner
# Minst tre mulige utfall er påkrevd
if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print("Utfall: Sterkt samarbeid. Teamet leverer i tide.")
elif valg1 == "1" and valg2 == "2" and valg3 == "2":
    print("Utfall: Leveranse skjer. Samarbeidet trenger videre arbeid.")
elif valg1 == "2" and valg3 == "2":
    print("Utfall: Formell prosess gir lav motivasjon.")
elif valg1 == "u" or valg2 == "u" or valg3 == "u":
    print("Utfall: Uklare valg gir usikker retning i prosjektet.")
else:
    print("Utfall: Delvis løst situasjon. Flere punkter krever oppfølging.")

# Oppsummering av alle valg
print("\nOppsummering:")
print(" Beslutning 1:", choice1)
print(" Beslutning 2:", choice2)
print(" Beslutning 3:", choice3)

print("\nProgram slutt.")
