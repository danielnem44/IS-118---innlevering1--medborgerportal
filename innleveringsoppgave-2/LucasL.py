# Interaktiv historie: Erling som prosjektleder
print("Hei! Nå skal du hjelpe Erling med å styre prosjektgruppen sin.")
print("Du får tre situasjoner der du må velge hva Erling skal gjøre.\n")

# Første konflikt: Silje og Sivert
print("Situasjon 1: Silje og Sivert er uenige og samarbeidet rakner.")
valg1 = input("Hva gjør Erling? Skrive 'snakke' for en samtale, eller 'HR' for å hente inn hjelp: ").lower()

# Andre konflikt: Jabir og Hamid
print("\nSituasjon 2: Jabir og Hamid står fast i en diskusjon om digital medvirkning.")
valg2 = input("Hvordan reagerer Erling? Skriv 'møte' for å samle dem, eller 'vente' for å se om de løser det selv: ").lower()

# Tredje tema: Teamet begynner å bli slitent
print("\nSituasjon 3: Teamet virker utbrent og litt demotivert.")
valg3 = input("Hva prioriterer Erling? Skriv 'pause' for en aktivitet eller 'fokus' for å pushe mot leveranse: ").lower()

print("\n=== UTFALL ===")

# Full harmoni
if valg1 == "snakke" and valg2 == "møte" and valg3 == "pause":
    print("Erling skaper trygghet og struktur. Teamet finner tilbake til roen og beveger seg i retning av Norming-fasen.")

# Leveranse-for-sentrert valg
elif valg3 == "fokus":
    if valg1 == "hr" or valg2 == "vente":
        print("Prosjektet blir levert som planlagt, men samarbeidsklimaet blir skjørt og slitne teammedlemmer mister motivasjon.")
    else:
        print("Leveransen går igjennom, men stemningen i teamet blir anspent og energinivået faller.")

# Delvis bra, delvis dårlig
else:
    print("Noen problemer blir løst, men konfliktene ligger fortsatt i lufta. Teamet fungerer, men mangler stabilitet.")