def invertir_cadena(cadena):
    cadena = list(cadena)
    if "+" in cadena:
        cadena.remove("+")
        cadena.append("+")
        strA = "".join(cadena)
        return strA[::-1]
    elif "-" in cadena:
        cadena.remove("-")
        cadena.append("-")
        strA = "".join(cadena)
        return strA[::-1]
    else:
        strA = "".join(cadena)
        return strA[::-1]

A = str(input("Dame un valor: "))

print(invertir_cadena(A))

if(A == invertir_cadena(A)):
    print ("True")
else:
    print ("False")
