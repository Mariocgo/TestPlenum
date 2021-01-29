def valido_Num(Num):
    if int(Num)<2147483647 and int(Num)>-2147483648:
        return invertir_cadena(Num)

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

# el dato a ingresar se escribe en el codigo
print(valido_Num("10"))