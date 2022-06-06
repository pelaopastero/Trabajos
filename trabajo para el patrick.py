op=0
while op!=4:
    print("1-.administración general")
    print("2-.inglés")
    print("3-.legunaje")
    print("4-.salir")
    print("\n")

    try:

        op=int(input("elija que desea estudiar:  "))

        if op==1:
            print("La administración general pertenece a las ciencias sociales que tiene como propósito el análisis de las organizaciones, a través de la planificación, organización, dirección y control de los recursos económicos, materiales, tecnológicos y humanos.")
            print("\n")
        elif op==2:
            print("1-.Separa las palabras en sílabas")
            print("2-.No tengas miedo de hablar")
            print("3-.Ve vídeos, Escucha")
            print("4-.Presta atención a la entonación y a los acentos")
            print("5-.Lee en voz alta mientras te grabas")
            print("6-.Imita un monólogo de una película")
            print("7-.Habla despacio.")
            print("\n")
        elif op==3:
            print("Sobresdrújula / A todas se les marca la tilde")
            print("Esdrújula / A todas se les marca la tilde")
            print("Graves	/ Tilde cuando terminan en consonante diferente a n, s y vocal")
            print("Agudas / Tilde cuando terminan n, s y vocal")    
            print("\n")
    except ValueError:
        print("ingrese la opcion correcta")
    except  TypeError: 
        if (op>4):
            print("elija una opcion del 1 al 4")      
print("gracias por estudiar conmigo")
