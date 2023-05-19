from pojistena_osoba import Pojistena_osoba

pojistenci = []

pokracovat = "ano"

while pokracovat == "ano":
    try:
        moznost = int(
            input("\n---------------------------- \n     Evidence pojištěných     \n---------------------------- \n "
                  "Vyberte si z nabízených možností: \n"
                  "1. Přidat novou pojištěnou osobu\n"
                  "2. Vypsat všechny pojištěné osoby\n"
                  "3. Vyhledat pojištěnou osobu\n"
                  "4. Ukončit aplikaci\n"
                  "\nZde prosím zadejte vybranou možnost: "))

        if moznost == 1:
            jmeno = input("Zadejte křestní jméno pojištěné osoby: ")
            prijmeni = input("Zadejte přijmení pojištěné osoby: ")
            vek = int(input("Zadejte věk pojištěné osoby: "))
            tel_cislo = int(input("Zadejte telefonní číslo pojištěné osoby: "))

            nova_pojistena_osoba = Pojistena_osoba(jmeno, prijmeni, vek, tel_cislo)
            print(nova_pojistena_osoba)
            print("\nNová pojištěná osoba byla právě nahrána.")
            pojistenci.append(nova_pojistena_osoba)
            pokracovat = input("\nPřejete si dále pokračovat? ano/ne\n")

        elif moznost == 2:
            for nova_pojistena_osoba in pojistenci:
                print(nova_pojistena_osoba)
            pokracovat = input("\nPřejete si dále pokračovat? ano/ne\n")


        elif moznost == 3:
            zadavane_jmeno = input("Zadejte jméno: ")
            zadavane_prijmeni = input("Zadejte přijmení: ")

            for nova_pojistena_osoba in pojistenci:
                if nova_pojistena_osoba.jmeno == zadavane_jmeno.capitalize() and \
                        nova_pojistena_osoba.prijmeni == zadavane_prijmeni.capitalize():
                    print(nova_pojistena_osoba)
                    print("\nPojištěná osoba existuje")

                else:
                    print("\nOsoba {0} {1} není v evidencii".format(zadavane_jmeno, zadavane_prijmeni))
            pokracovat = input("\nPřejete si dále pokračovat? ano/ne\n")

        elif moznost == 4:
            pokracovat = "Ne"

        else:
            print("\nZadali jste nesprávnou možnost!")
            pokracovat = input("\nPřejete si dále pokračovat? ano/ne\n")

    except ValueError as e:  # Chybové hlášení v momentě, kdy se v aplikaci v inputu zadá string místo integeru
        print("Zadali jste nesprávnou možnost.")
        pokracovat = input("\nPřejete si dále pokračovat? ano/ne\n")

ukonceni = input("Evidence pojištěných osob se nyní uzavře po stiskuní libovolné klávesy")
