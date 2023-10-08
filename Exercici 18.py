
# Realitza un programa que demani el dia de la setmana (de l'1 a l'7) i escriviu el dia corresponent.
# Si introduïm un altre número ens dóna un error.

dia = int(input("Posa el nombre de un dia de la setmana: "))

setmana = {1: "dilluns", 2: "dimarts", 3: "dimecres", 4: "dijous", 5: "divendres", 6: "disabte", 7: "diumenge" }

if dia in setmana:
    print(f"El dia de la setmana que has posat es: {setmana[dia]}")

if dia not in setmana:
    print("Ha posat un dia que no existeix.")
