
#La política de cobrament d'una companyia telefònica és: quan es realitza una trucada, el cobrament és pel temps que
#aquesta dura, de tal manera que els primers cinc minuts costen 1 euro, els següents 3, 80 cèntims, els següents dos
#minuts, 70 cèntims, i a partir del desè minut, 50 cèntims.

#A més a més, es carrega un impost de 3% quan és diumenge, i si és un altre dia, en torn de matí, 15%, i en torn
#de tarda, 10%. Feu un algoritme per determinar quant ha de pagar per cada concepte una persona que realitza una trucada.


temps = int(input("Introdueix el temps de la trucada: "))
dia = str(input("Introdueix en dia que es va fer la trucada: "))
torn = str(input("Introdueix el torn en el que es va fer la trucada (mati o tarda): "))

#Preu trucada.

preu = 0

#Primer 5 minuts i la resta es va sumant.

cinc_minuts = 1
tres_minuts = 0.80
dos_minuts = 0.70
deu_minuts = 0.50

#Dia i torn.

entre_setmana = ["dilluns","dimarts", "dimecres", "dijous","divendres", "dissabte"]

torn_mati = 0.10
torn_tarda = 0.15
diumenge = 0.3

#Condicions


if temps > 0 and temps <=5:
    preu += cinc_minuts
    if dia in entre_setmana and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == "diumenge" and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    elif dia in entre_setmana and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == diumenge and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    else:
      print("Error: No ha posat corrcetament alguna de les dades.")


elif temps > 5 and temps <= 8:
    preu += tres_minuts + cinc_minuts
    if dia in entre_setmana and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == "diumenge" and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    elif dia in entre_setmana and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == 'diumenge' and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    else:
        print("Error: No ha posat corrcetament alguna de les dades.")


elif temps > 8 and temps < 10:
    preu += tres_minuts + cinc_minuts + dos_minuts
    if dia in entre_setmana and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == 'diumenge' and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    elif dia in entre_setmana and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == 'diumenge' and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    else:
      print("Error: No ha posat corrcetament alguna de les dades.")

elif temps >= 10:
    preu += tres_minuts + cinc_minuts + dos_minuts + deu_minuts
    deu_en_adelant = temps - 9
    preu_per_minut = deu_en_adelant * deu_minuts
    preu+= preu_per_minut
    if dia in entre_setmana and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == 'diumenge' and torn == "mati":
        percentatge_mati = preu * torn_mati
        preu += percentatge_mati + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    elif dia in entre_setmana and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda
        print(f"La trucada ha surtit en {preu:.3}€")
    elif dia == 'diumenge' and torn == "tarda":
        percentatge_tarda = preu * torn_tarda
        preu += percentatge_tarda + diumenge
        print(f"La trucada ha surtit en {preu:.3}€")

    else:
      print("Error: No ha posat corrcetament alguna de les dades.")


