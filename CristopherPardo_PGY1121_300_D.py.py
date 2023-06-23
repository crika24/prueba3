print("Ingrese una opcion \n 1) Grabar \n 2) Buscar \n 3) Imprimir certificado \n 4) Salir")
op=int(input())
lista=[]
if op==1:
    vehiculo=input("ingrese detalles de su veihulo: tipo, patente, marca (debe tener 2 a 15 caracteres), precio (debe ser mayor a $5.000.000), multa, fecha de multa, fecha de registro y nombre del dueño: \n NOTA: AL INGRESAR LOS DETALLES DEL VEHICULO DEBE SEPARAR POR (,)\n").split(",")
    for i in vehiculo:
        lista.append(i)
    print(lista)
    while len(lista[2])<2 or len(lista[2])>15:
        print("Marca fuera de rango, Por favor ingrese nuevamente los datos")
        vehiculo=input().split(",")
    else:
        print("Patente dentro del rango de caracteres")
    while int(lista[3])<5000000:
        print("Dinero fuera de lo requerido, Por favor ingrese nuevamente los datos")
        vehiculo=input().split(",")
    else:
        print("Dinero ingresado correcto")

    a=vehiculo
print(a)  
if op==2:
    print(a)
    
        


