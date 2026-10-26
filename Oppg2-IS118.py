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
        print("2. Uenigheten mellom Hamdi og Hallgeir")

    if not situasjon_3_ferdig:
        print("3. Motivasjon")

    valg = input("Velg situasjon: ")

    if valg == "1" and not situasjon_1_ferdig:

        while True:

            print("KONFLIKT 1")
            print("1. Valg 1")
            print("2. Valg 2")
            print("3. Valg 3")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Konsekvens av valg 1")
                poeng += 3
                situasjon_1_ferdig = True
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 2
                situasjon_1_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
                poeng += 1
                situasjon_1_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "2" and not situasjon_2_ferdig:

        while True:

            print("KONFLIKT 2")
            print("1. Snakke med begge hver for seg, deretter ha et felles møte.")
            print("2. Ikke blande seg inn og la Hamdi og Hallgeir løse konflikten selv.")
            print("3. Arrangere et felles møte, vurdere begge forslagene og finne en løsning sammen.")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Mulig positiv konsekvens: Erling forstår konflikten bedre, og et felles møte hjelper dem med å finne en løsning. Konflikten løses, og fremdriften fortsetter som planlagt.")
                print("Mulig negativ konsekvens: Hamdi eller Hallgeir kan føle at Erling tar parti. Dette kan skape mistillit, baksnakking og forsinkelser i prosjektet.")
                poeng += 15
                situasjon_2_ferdig = True
                break

            elif svar == "2":
                print("Mulig positiv konsekvens: Hamdi og Hallgeir finner en løsning på egen hånd. Tilliten styrkes, og prosjektet fortsetter som planlagt.")
                print("Mulig negativ konsekvens: De klarer ikke å løse konflikten, kollegaene velger side, og samarbeidet svekkes. Dette kan føre til forsinkelser i prosjektet.")
                poeng += 5
                situasjon_2_ferdig = True
                break

            elif svar == "3":
                print("Mulig positiv konsekvens: Hamdi og Hallgeir får forklart synspunktene sine og finner en løsning som kombinerer begge forslagene. Samarbeidet styrkes, og prosjektet fortsetter som planlagt.")
                print("Mulig negativ konsekvens: Hamdi og Hallgeir blir fortsatt uenige og klarer ikke å inngå kompromiss. Dette skaper frustrasjon og forsinker arbeidet med prototypen.")
                poeng += 10
                situasjon_2_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    elif valg == "3" and not situasjon_3_ferdig:

        while True:

            print("MOTIVASJON")
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

