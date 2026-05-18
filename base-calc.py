def menu():
 print("Bienvenido. Aqui tienes las opciones:")
 print("1. Suma                      2. Resta")
 print("3. Multiplicacion            4. Division")
 mango=int(input("Elija: "))
 if mango==1:
     print("Utilize suma(*primer numero*, *segundo numero*) para la operacion")
 else:
     if mango==2:
         print("Utilize resta(*primer numero*, *segundo numero*) para la operacion")
     else:
         if mango==3:
             print ("Multiplicación")
             multi1 = float(input("Ingrese el primer número: "))
             multi2 = float(input("Ingrese el segundo número: "))

             Resultadomulti = multi1 * multi2

             print ("El resultado de tu multiplicación es: ", Resultadomulti)
             
         else:
             if mango==4:
                 print("División")
                 divi1 = float(input("Ingrese el primer número: "))
                 divi2 = float(input("Ingrese el segundo número: "))
                 resultadodiv= divi1/divi2
                 print ("El resultado de la división es: " , resultadodiv)
                 
             else:

                 print("No es una opcion")       
def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def TODO():
    print("¡FUNCION EN PROCESO!")

