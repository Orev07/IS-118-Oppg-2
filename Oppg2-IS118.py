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
        print("1. Konflikt mellom Silje og Elias")

    if not situasjon_2_ferdig:
        print("2. Uenighet mellom Hamdi og Hallgeir ")

    if not situasjon_3_ferdig:
        print("3. Opprettholde motivasjon i teamet")

    valg = input("Velg situasjon: ")

    if valg == "1" and not situasjon_1_ferdig:
#vil bare være mulig og entre situasjonen vis den er true, når den er false vil det ikke vøre mulig og entre den med et uhell
        while True:

            print("Den første konflikten Erling må håndtere, er konflikten mellom Silje og Elias. Denne konflikten har eskalert seg til en personkonflikt og påvirker resten av teame. Hva burde Erling gjøre nå?")
            print("1. Erling snakker med Silje og Elias hver for seg for å forstå begge perspektivene. ")
            print("2. Erling samler Silje og Elias for å diskutere uenigheten sammen.")
            print("3. Erling velger Elias sin tekniske løsning, men lar Silje foreslå mindre designforbedringer innenfor budsjettet.")

            svar = input("Velg alternativ: ")

            if svar == "1":
                print("Erling får bedre innsikt i konflikten, men det kan ta lengre tid før teamet kommer fram til en felles løsning.")
                poeng += 15
                situasjon_1_ferdig = True
                #break gjør at while-løkken til konfliktene stopper, slik at man ikke ender opp i en evig loop i samme konflikt
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

            print("KONFLIKT 2 Hamdi og Hallgeir er uenige om hvordan digitale folkemøter skal gjennomføres, og Erling må finne en måte å løse konflikten på.")
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

