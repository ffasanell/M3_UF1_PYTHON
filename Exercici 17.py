
# Realitza un programa que demani per teclat el resultat (dada sencer) obtingut a llançar un dau de sis cares i mostri
# per pantalla el nombre en lletres (dada cadena) de la cara oposada al resultat obtingut.

# Nota 1: En les cares oposades d'un dau de sis cares estan els números: 1-6, 2-5 i 3-4.
# Nota 2: Si el nombre del dau introduït és menor que 1 o més gran que 6, es mostrarà el missatge: "ERROR: nombre
# incorrecte.".

# exemple:
# Introduïu nombre de el dau: 5
# A la cara oposada hi ha el "dos".

cara =  int(input("Posar un nombre del 1 al 6: "))

caras = {1: 6, 2: 5, 3: 4, 6: 1, 5: 6, 4:3}


if cara < 1 or cara > 6:
    print("ERROR: nombre incorrecte")

elif cara in caras:
    print(f"La cara oposada es:{caras[cara]}")









