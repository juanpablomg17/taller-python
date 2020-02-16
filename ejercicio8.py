
var = True 
while var == True:
    opcion = int(input("------------------------------\n Sistema de conversion \n 1. De a pesos colombianos a dolares \n 2. De pesos colombiandos a euros \n 3. de Pesos colombianos a bit coins  "))

    if opcion == 1:
        dolaractual = float(input("cuál es el valor actual del dolar en pesos colombianos. \n tenga en cuenta la relacion 1 peso = x cantidad de euros"))
        peso = float(input("por favor digite la cantidad de pesos a convertir a dólares"))
        dolar = peso * dolaractual
        print("la cantidad de dólares es de : ",dolar, "$")
 


    if opcion == 2:
        valoreuro = float(input("cuál es el valor actual del euro en pesos colombianos. \n tenga en cuenta la relacion 1 peso = x cantidad de euros"))
        peso = float(input("por favor digite la cantidad de pesos a convertir"))
        euro = peso * valoreuro
        print("la cantidad de euros es de : ",euro,  "€")


    if opcion == 3:
        peso = float(input("por favor digite la cantidad de pesos a convertir"))
        bitcoin = peso * 2.9e-8
        print("la cantidad de bitcoins es de : ",bitcoin, "฿")

    if opcion == 4:
        print("See you later :), have a nice day ")
        var = False

    else {

        print("opción inválida, intenta de nuevo")
    }














