def seleccionar_animal():
    print("Bienvenido al juego de selección de animales.")
    print("Usa las teclas de dirección (arriba, abajo, izquierda, derecha) para moverte.")
    print("Tu objetivo es llegar al animal correcto.")
    
    # Nivel 1
    print("\nEstás en el inicio.")
    #print("Mover hacia la derecha para Mamíferos, abajo para Reptiles, izquierda para Peces, arriba para Aves.")
    direccion = input("Ingresa la dirección: ")

    if direccion == "derecha":
        print("Te has movido a Mamíferos.")
        #print("Mover hacia arriba para Domésticos, abajo para Salvajes, derecha para Acuáticos.")
        direccion_mamifero = input("Ingresa la dirección: ")

        if direccion_mamifero == "arriba":
            print("Has seleccionado Mamíferos Domésticos.")
            #print("Mover hacia derecha para Perro, abajo para Gato, izquierda para Conejo.")
            direccion_domestico = input("Ingresa la dirección: ")

            if direccion_domestico == "derecha":
                print("Has llegado a: Perro 🐕")
            elif direccion_domestico == "abajo":
                print("Has llegado a: Gato 🐈")
            elif direccion_domestico == "izquierda":
                print("Has llegado a: Conejo 🐇")
            else:
                print("Opción no válida.")
        elif direccion_mamifero == "abajo":
            print("Has seleccionado Mamíferos Salvajes.")
            #print("Mover hacia arriba para León, derecha para Elefante, izquierda para Tigre.")
            direccion_salvaje = input("Ingresa la dirección: ")

            if direccion_salvaje == "arriba":
                print("Has llegado a: León 🦁")
            elif direccion_salvaje == "derecha":
                print("Has llegado a: Elefante 🐘")
            elif direccion_salvaje == "izquierda":
                print("Has llegado a: Tigre 🐅")
            else:
                print("Opción no válida.")
        elif direccion_mamifero == "derecha":
            print("Has seleccionado Mamíferos Acuáticos.")
            #print("Mover hacia derecha para Delfín, abajo para Ballena, izquierda para Foca.")
            direccion_acuatico = input("Ingresa la dirección: ")

            if direccion_acuatico == "derecha":
                print("Has llegado a: Delfín 🐬")
            elif direccion_acuatico == "abajo":
                print("Has llegado a: Ballena 🐋")
            elif direccion_acuatico == "izquierda":
                print("Has llegado a: Foca 🦭")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida.")

    elif direccion == "abajo":
        print("Te has movido a Reptiles.")
        #print("Mover hacia arriba para Domésticos, derecha para Salvajes, abajo para Acuáticos.")
        direccion_reptil = input("Ingresa la dirección: ")

        if direccion_reptil == "arriba":
            print("Has seleccionado Reptiles Domésticos.")
            #print("Mover hacia derecha para Tortuga, abajo para Iguana.")
            direccion_domestico_reptil = input("Ingresa la dirección: ")

            if direccion_domestico_reptil == "derecha":
                print("Has llegado a: Tortuga 🐢")
            elif direccion_domestico_reptil == "abajo":
                print("Has llegado a: Iguana 🦎")
            else:
                print("Opción no válida.")
        elif direccion_reptil == "derecha":
            print("Has seleccionado Reptiles Salvajes.")
            #print("Mover hacia arriba para Cocodrilo, derecha para Serpiente, izquierda para Camaleón.")
            direccion_salvaje_reptil = input("Ingresa la dirección: ")

            if direccion_salvaje_reptil == "arriba":
                print("Has llegado a: Cocodrilo 🐊")
            elif direccion_salvaje_reptil == "derecha":
                print("Has llegado a: Serpiente 🐍")
            elif direccion_salvaje_reptil == "izquierda":
                print("Has llegado a: Camaleón 🦎")
            else:
                print("Opción no válida.")
        elif direccion_reptil == "abajo":
            print("Has seleccionado Reptiles Acuáticos.")
            #print("Mover hacia derecha para Lagarto Acuático, abajo para Serpiente de Mar.")
            direccion_acuatico_reptil = input("Ingresa la dirección: ")

            if direccion_acuatico_reptil == "derecha":
                print("Has llegado a: Lagarto Acuático 🦎")
            elif direccion_acuatico_reptil == "abajo":
                print("Has llegado a: Serpiente de Mar 🐍")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida.")

    elif direccion == "izquierda":
        print("Te has movido a Peces.")
        #print("Mover hacia arriba para Tiburón, derecha para Pez Payaso, abajo para Manta Raya.")
        direccion_pez = input("Ingresa la dirección: ")

        if direccion_pez == "arriba":
            print("Has llegado a: Tiburón 🦈")
        elif direccion_pez == "derecha":
            print("Has llegado a: Pez Payaso 🐠")
        elif direccion_pez == "abajo":
            print("Has llegado a: Manta Raya 🏞️")
        else:
            print("Opción no válida.")

    elif direccion == "arriba":
        print("Te has movido a Aves.")
        print("Mover hacia derecha para Domésticas, izquierda para Salvajes.")
        direccion_ave = input("Ingresa la dirección: ")

        if direccion_ave == "derecha":
            print("Has seleccionado Aves Domésticas.")
            #print("Mover hacia derecha para Gallina, abajo para Canario.")
            direccion_domestico_ave = input("Ingresa la dirección: ")

            if direccion_domestico_ave == "derecha":
                print("Has llegado a: Gallina 🐔")
            elif direccion_domestico_ave == "abajo":
                print("Has llegado a: Canario 🐤")
            else:
                print("Opción no válida.")
        elif direccion_ave == "izquierda":
            print("Has seleccionado Aves Salvajes.")
            #print("Mover hacia derecha para Águila, abajo para Buitre.")
            direccion_salvaje_ave = input("Ingresa la dirección: ")

            if direccion_salvaje_ave == "derecha":
                print("Has llegado a: Águila 🦅")
            elif direccion_salvaje_ave == "abajo":
                print("Has llegado a: Buitre 🦅")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida.")

    else:
        print("Opción no válida.")

# Ejecutamos el código
seleccionar_animal()