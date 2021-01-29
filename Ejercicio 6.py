lista=[]

NumEventos=int(input("Ingrese el numero de eventos:"))

for x in range(NumEventos):
    valor=str(input("Ingrese las fechas del evento:"))
    if "," in valor:
        print("Hay una coma")
        valor=list(valor)
        valor.remove(",")
        print(valor)
    else:
        contador+=x
        print("No hay una coma")
        lista.append(valor)
        
    
print(len(lista))