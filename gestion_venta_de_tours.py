from class_cliente import Cliente 

def buy_tour(clientes, total_cupos, option):
    """ Esta funcion se encarga de vender los tours de los cruceros. Inicialmente se pide el ingreso del DNI del cliente, para luego imprimir los tours ofrecidos y si se selecciona uno se piden la cantidad de personas.
        Se ingresar los datos del cliente en la base de datos de tour ('Database_Clientes.p') y luego estos se registran en la base de datos de los tours del crucero ('Database_Cupos.p').


    Args:
        clientes --> Diccionario de clientes que han realizado una compra de tour.
        total_cupos --> Diccionario de la cantidad de tour que sobran por crucero.
        option --> Numero correspondiente a su crucero del cliente.

    Retorna--> Los datos modificados de los diccionarios (clientes y total_cupos) y una impresión de el tour comprado, la hora que empieza y el precio.
    """
    if option == '1':
        key  = 'El Dios de los Mares'
    elif option == '2':
        key  = 'La Reina Isabel'
    elif option == '2':
        key  = 'El Libertador del Océano'
    else:
        key  = 'Sabas Nieves'

    while True:
        try:
            dni = int(input('\n Ingrese el DNI del cliente:  '))
            break
        except:
            print('Error, ingrese el DNI de nuevo.')

    # ciclo que me permite repetir el cogió si se quiere seguir realizado cualquiera de las operaciones.
    while True:
        # ELECCIÓN que me permite saltar a la operación a realzar. 
        elección = input('''\n Bienvenido a Saman Caribbean Tours 🛳️.
          ¿Que tour desea realizar? 
        \n 1. Tour en el puerto.
 (Precio: $30/persona. Max: 4 personas. Descuento: si. Hora: 7 A.M.)
        \n 2. Degustación de comida local.
 (Precio: $100/persona. Max: 2 personas. Hora: 7 A.M.)
        \n 3. Trotar por el pueblo/ciudad.
 (Precio: gratis. Hora: 6 A.M.)
        \n 4. Visita a lugares historicos. 
 (Precio: $40/persona. Max: 4 personas. Descuento: si. Hora: 10 A.M.)
        \n 5. Salir.
        > ''')
        while elección != "1" and elección != "2" and elección != "3" and elección != "4" and elección != "5":
            elección = input(" Ingrese un numero válido [1,5]: ")

        if elección == '1':
            time = '7 A.M'
            tour = 'en el puerto'
            while True:
                try:
                    cupos = int(input(' Ingrese el numero de personas (maximo 4 personas): '))
                    if cupos <= 0 or cupos > 4:
                        pass
                    else:
                        break
                except:
                    print(' Error, ingrese un numero.')
           
            if (total_cupos[key]['en el puerto'] - cupos) > 0:
                total_cupos[key]['en el puerto'] -= cupos
            else:
                print(' Limites de cupos ya ha sido alcanzado')
                break
            
            if cupos == 3:
                total_price = cupos*30 - (30*0.1)
            elif cupos == 4:
                total_price = cupos *30 - (60*0.1)
            else:
                total_price = cupos *30
            
        elif elección == '2':
            time = '12 P.M'
            tour = 'degustación de comida local'
            while True:
                try:
                    cupos = int(input(' Ingrese el numero de personas (maximo 2 personas): '))
                    if cupos <= 0 or cupos > 2:
                        pass
                    else:
                        break
                except:
                    print(' Error, ingrese un numero.')
            total_price = cupos *100

            if (total_cupos[key]['degustación de comida local'] - cupos) > 0:
                total_cupos[key]['degustación de comida local'] -= cupos
            else:
                print(' Limites de cupos ya ha sido alcanzado')
                break

        elif elección == '3':
            time = '6 A.M'
            tour = 'trotar por el pueblo/ciudad'
            while True:
                try:
                    cupos = int(input(' Ingrese el numero de personas: '))
                    if cupos <= 0:
                        pass
                    else:
                        break
                except:
                    print(' Error, ingrese un numero.')
            total_price = cupos *0
            total_cupos[key]['trotar por el pueblo/ciudad'] += cupos
            
        elif elección == '4':
            time = '10 A.M'
            tour = 'visita a lugares historicos'
            while True:
                try:
                    cupos = int(input(' Ingrese el numero de personas (maximo 4 personas): '))
                    if cupos <= 0 or cupos > 4:
                        pass
                    else:
                        break
                except:
                    print(' Error, ingrese un numero.')
            if cupos >= 3:
                total_price = cupos*40 -(cupos*40*(0.1))
            else:
                total_price = cupos*40
            
            if (total_cupos[key]['visita a lugares históricos'] - cupos) > 0:
                    total_cupos[key]['visita a lugares históricos'] -= cupos
            else:
                print(' Limites de cupos ya ha sido alcanzado')
                break

        else:
            print("\n")
            break
        
        crucero = key
        cliente = Cliente(dni, tour, total_price, time, crucero)
        clientes[cliente.dni] = [cliente.tour, cliente.total_price, cliente.time, cliente.crucero]
        print(f'\n El tour {cliente.tour} empieza a las {cliente.time}.\n Monto Total: ${cliente.total_price} \n')
        return clientes, total_cupos
