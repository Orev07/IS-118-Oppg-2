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
        print("1. Konflikt 1")

    if not situasjon_2_ferdig:
        print("2. Konflikt 2")

    if not situasjon_3_ferdig:
        print("3. Hvordan bevare motivasjonen i teamet?")

    valg = input("Velg situasjon: ")

    if valg == "1" and not situasjon_1_ferdig:

        while True:

            print("")
            print("1.")
            print("2.")
            print("3.")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("")
                poeng += 3
                situasjon_1_ferdig = True
                break

            elif svar == "2":
                print("")
                poeng += 2
                situasjon_1_ferdig = True
                break

            elif svar == "3":
                print("") 
                poeng += 1
                situasjon_1_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "2" and not situasjon_2_ferdig:

        while True:

            print("KONFLIKT 2")
            print("1. Valg 1")
            print("2. Valg 2")
            print("3. Valg 3")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Konsekvens av valg 1")
                poeng += 3
                situasjon_2_ferdig = True
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 2
                situasjon_2_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
                poeng += 1
                situasjon_2_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "3" and not situasjon_3_ferdig:

        while True:

            print("Hvordan bevare motivasjonen i teamet?")
            print("1. Vil du prioritere relasjonsbygging og tydelig kommunikasjon ved å samle teamet for å avklare mål, roller og samarbeid?")
            print("2. Vil du prioritere fremdrift og leveranser for å sikre at prototypen blir ferdig innen fristen?")
            print("3. Vil du fordele konkrete arbeidsoppgaver og delmål og følge opp fremdriften gjennom korte statusmøter?")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Tilliten og samarbeidet i teamet styrkes, men du får mindre tid til arbeidet med prototypen.")
                poeng += 15
                situasjon_3_ferdig = True
                break

            elif svar == "2":
                print("Teamet arbeider mer effektivt på kort sikt, men uløste konflikter svekker motivasjonen og samarbeidet.")
                poeng += 5
                situasjon_3_ferdig = True
                break

            elif svar == "3":
                print("Teamet får bedre struktur og motivasjon, men tett oppfølging og stor arbeidsmengde skaper ekstra press.")
                poeng += 10
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

