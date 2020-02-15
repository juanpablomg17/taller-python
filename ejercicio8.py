
var = True 
while var == True:
    opcion = int(input("------------------------------\n Sistema de conversion \n 1. De a pesos colombianos a dolares \n 2. De pesos colombiandos a euros \n 3. de Pesos colombianos a bit coins  "))

    if opcion == 1:
        peso = float(input("por favor digite la cantidad de pesos a convertir"))
        dolar = peso * 0.00030
        print("la cantidad de dólares es de : ",dolar, "$")
 


    if opcion == 2:
        valoreuro = input("por favor digite el valor actual del euro en pesos colombianos") 
        peso = float(input("por favor digite la cantidad de pesos a convertir"))
        euro = peso * valoreuro
        print("la cantidad de euros es de : ",euro,  "€")


    if opcion == 3:
        peso = float(input("por favor digite la cantidad de pesos a convertir"))
        bitcoin = peso * 2.9e-8
        print("la cantidad de bitcoins es de : ",bitcoin, "฿")

    if opcion == 4:
        print("See you later :) ")
        var = False














