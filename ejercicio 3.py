def es_palindromo(cadena):
    cadConvertina  = cadena.lower()
    posPalindromo = cadConvertina[::-1]

    if posPalindromo == cadConvertina:
        return  bool(True)
    else:
        return bool(False)


if es_palindromo(input("Ingrese una cadena palindromo: ")):
    print("La cadena es un palindromo")
else:
    print("La cadena NO es un palindromo")