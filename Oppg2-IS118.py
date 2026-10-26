poeng = 0
#false gjør at situasjonene ikke er gjennomført enda
situasjon_1_ferdig = False
situasjon_2_ferdig = False
situasjon_3_ferdig = False

print("ERLINGS UTFORDRINGER")
print("Du er prosjektleder Erling.")
print("Du må håndtere tre ulike situasjoner.")

#not false = true, så da vil løkken starte
#når alle situasjoenene blir true, blir not true= false, og løkken vil stoppe
while not (
    situasjon_1_ferdig and
    situasjon_2_ferdig and
    situasjon_3_ferdig
):

    print("Velg hvilken situasjon du vil jobbe med med et tall fra 1-3:")
#om situasjoenene er false vil den printes pga, not false = true
    if not situasjon_1_ferdig:
        print("1. Konflikt 1")

    if not situasjon_2_ferdig:
        print("2. Konflikt 2")

    if not situasjon_3_ferdig:
        print("3. Motivasjon")

    valg = input("Velg situasjon: ")

    if valg == "1" and not situasjon_1_ferdig:
#vil bare være mulig og entre situasjonen vis den er true, når den er false vil det ikke vøre mulig og entre den med et uhell
        while True:

            print("KONFLIKT 1")
            print("1. Valg 1")
            print("2. Valg 2")
            print("3. Valg 3")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Konsekvens av valg 1")
                poeng += 15
                situasjon_1_ferdig = True
                #break gjør at while-løkken til konfliktene stopper, slik at man ikke ender opp i en evig loop i samme konflikt
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 5
                situasjon_1_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
                poeng += 10
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
                poeng += 15
                situasjon_2_ferdig = True
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 5
                situasjon_2_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
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
                poeng += 15
                situasjon_3_ferdig = True
                break

            elif svar == "2":
                print("Konsekvens av valg 2")
                poeng += 5
                situasjon_3_ferdig = True
                break

            elif svar == "3":
                print("Konsekvens av valg 3")
                poeng += 10
                situasjon_3_ferdig = True
                break

            else:
                print("Ugyldig valg. Prøv igjen.")

    else:
        print("Ugyldig valg eller situasjonen er allerede gjennomført.")

print(f"TOTAL POENGSUM: {poeng}")

if poeng >= 35:
    print("VIDERE TIL NORMING-FASEN:")
    print("Teamet gjenoppretter tilliten og går videre til norming-fasen. Strålende:)")

elif poeng >= 25:
    print("PÅ VEI MOT FORBEDRING:")
    print("Konfliktene er delvis løst, men relasjonene er fortsatt sårbare. Nesten der ;)")

else:
    print("FAST LÅST I STORMING-FASEN")
    print("Prosjektet mister samhold og blir forsinket. Her må nok noen valg revurderes :/")

