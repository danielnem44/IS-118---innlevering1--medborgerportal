print("Erling er leder for utviklingen av medborgerportalen.")
print("Etter seks uker har teamet kommet i storming fasen.")
print("Det er press på teamet på grunn av konflikter og ulike syn.\n")

print("Første situasjon oppstår. Silje og Sivert er uenige om design og løsning.")
print("Erling må velge hvordan han vil ta dette videre.\n")

print("1: Ta konflikten i plenum")
print("2: Ha individuelle samtaler")

valg1 = input("Skriv 1 eller 2: ")
konflikt = ""

if valg1 == "1":
    print("Erling tar det i fellesskap. Konflikten blir tydelig for alle.")
    konflikt = "apen"
else:
    print("Erling tar samtaler hver for seg. Konfliktene minker litt.")
    konflikt = "dempet"

print("\nNy situasjon. Hamdi og Jabir er uenige om digital dialog.")
print("Uenigheten vokser sakte. Erling må ta et nytt valg.\n")

print("1: Kalle inn begge til felles avklaring")
print("2: Ignorere og se hva som skjer")

valg2 = input("Skriv 1 eller 2: ")
uenighet = ""

if valg2 == "1":
    print("Erling samler begge. Uenigheten kommer fram og blir tydelig.")
    uenighet = "avklart"
else:
    print("Erling ignorerer. Spenningen ligger i bakgrunnen.")
    uenighet = "logende"

print("\nNy situasjon. Teamet virker slitent. Energien synker.")
print("Prototypen skal være klar om tre uker. Erling må sikre motivasjonen.\n")

print("1: Prioritere relasjonsbygging")
print("2: Prioritere leveranse og tempo")

valg3 = input("Skriv 1 eller 2: ")
motiv = ""

if valg3 == "1":
    print("Erling setter av tid til refleksjon og bedre normer for samarbeid.")
    motiv = "relasjon"
else:
    print("Erling presser mot levering og tydelige mål.")
    motiv = "leveranse"

print("\nSlutt:\n")

if konflikt == "dempet" and uenighet == "avklart" and motiv == "relasjon":
    print("Teamet får bedre samarbeidsklima. De går videre mot norming.")
elif motiv == "leveranse" and (konflikt == "apen" or uenighet == "logende"):
    print("Teamet leverer, men motivasjonen blir ustabil.")
else:
    print("Prosjektet mister samhold. Rekker ikke leveringsfristen.")
