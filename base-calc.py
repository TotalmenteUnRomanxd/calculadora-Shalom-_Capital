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
             print("Utilize multiplicacion(*primer numero*, *segundo numero*) para la operacion")
         else:
             if mango==4:
                 print("Utilize division(*primer numero*, *segundo numero*) para la operacion")
             else:

                 print("No es una opcion")       
def suma(a, b):
    resultado = a + b
print("el resultado de la suma es:"), resultado
return resultado
def resta(a, b):
    resultado = a - b
print("el resultado de la resta es:"), resultado
return resultado
def TODO():
    print("¡FUNCION EN PROCESO!")
