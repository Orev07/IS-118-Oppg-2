poeng = 0

situasjon_1_ferdig = False
situasjon_2_ferdig = False
situasjon_3_ferdig = False  

print("=== ERLINGS UTFORDRINGER ===")
print("Du er prosjektleder Erling.")
print("Du må håndtere tre ulike situasjoner.")

while not (
    situasjon_1_ferdig and
    situasjon_2_ferdig and
    situasjon_3_ferdig
):

    print("Velg hvilken situasjon du vil jobbe med:")

    if not situasjon_1_ferdig:
        print("1. Konflikt mellom Silje og Elias")

    if not situasjon_2_ferdig:
        print("2. Uenighet mellom Hamdi og Hallgeir ")

    if not situasjon_3_ferdig:
        print("3. Opprettholde motivasjon i teamet")

    valg = input("Velg situasjon: ")

    if valg == "1" and not situasjon_1_ferdig:

        while True:

            print("Den første konflikten du må håndtere, er konflikten mellom Silje og Elias. Denne konflikten har eskalert seg til en personkonflikt og påvirker nå resten av teamet.")
            print("1. Du snakker med Silje og Elias hver for seg for å forstå begge perspektivene. ")
            print("2. Du samler Silje og Elias for å diskutere uenigheten sammen.")
            print("3. Du velger Elias sin tekniske løsning, men lar Silje foreslå mindre designforbedringer innenfor budsjettet.")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Du vil få bedre innsikt i konflikten, men det kan ta lengre tid før teamet kommer fram til en felles løsning.")
                poeng += 15
                situasjon_1_ferdig = True
                break

            elif svar == "2":
                print("De får mulighet til å forstå hverandres synspunkter, men diskusjonen kan bli anspent dersom de føler seg kritisert.")
                poeng += 5
                situasjon_1_ferdig = True
                break

            elif svar == "3":
                print("Arbeidet kan fortsette som planlagt, men Silje kan føle at ideene hennes blir nedprioritert, slik at konflikten ikke blir helt løst.")
                poeng += 10
                situasjon_1_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "2" and not situasjon_2_ferdig:

        while True:

            print("Idividuelle samtaler og felles møte")
            print("1.Erling snakker først med Hamdi og Hallgeir hver for seg, før han samler dem for å diskutere mulige løsninger.")
            print("2.Erling lar Hamdi og Hallgeir forsøke å løse uenigheten på egen hånd. ")
            print("3. Erling bruker Hamdi sitt forslag som utgangspunkt, men lar Hallgeir foreslå endringer etter at løsningen er testet.")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Begge får forklart sitt syn, og de kan finne en løsning sammen. Samtidig kan de oppfatte samtalene som forskjellsbehandling dersom Erling ikke er tydelig og rettferdig.")
                poeng += 3
                situasjon_2_ferdig = True
                break

            elif svar == "2":
                print("De får mulighet til å løse konflikten selv, men dersom de ikke blir enige, kan uenigheten vokse og føre til dårligere samarbeid og forsinkelser.")
                poeng += 2
                situasjon_2_ferdig = True
                break

            elif svar == "3":
                print("Teamet får en tydelig retning og kan fortsette arbeidet, men Hallgeir kan føle at meningene hans blir nedprioritert, slik at konflikten ikke blir helt løst.")
                poeng += 1
                situasjon_2_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "3" and not situasjon_3_ferdig:

        while True:

            print("")
            print("1. Valg 1")
            print("2. Valg 2")
            print("3. Valg 3")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Konsekvens av valg 1")
                poeng += 3
                situasjon_3_ferdig = True
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 2
                situasjon_3_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
                poeng += 1
                situasjon_3_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    else:
        print("Ugyldig valg eller situasjonen er allerede gjennomført.")

print("===================")
print("TOTAL POENGSUM:", poeng)
print("===================")

if poeng >= 8:
    print("SLUTT 1")
    print("Teamet gjenoppretter tilliten og går videre til norming-fasen.")

elif poeng >= 5:
    print("SLUTT 2")
    print("Konfliktene er delvis løst, men relasjonene er fortsatt sårbare.")

else:
    print("SLUTT 3")
    print("Prosjektet mister samhold og blir forsinket.")

