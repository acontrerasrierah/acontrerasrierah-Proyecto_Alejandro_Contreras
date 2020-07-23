# Importar los Modulos
from gestion_de_cruceros import *
from gestion_de_habitaciones import *
from gestion_venta_de_tours import *
from gestion_del_restaurante import *
from gestion_de_estadisticas import *

# Librerías utilizadas:
import pickle

def main():
    # ciclo que me permite repetir el código si se quiere seguir realizado cualquiera de las operaciones.
    while True:
        # ELECCIÓN que me permite saltar a la operación a realzar. 
        elección = input(''' Bienvenido Saman Caribbean 🛳️.
            \n ¿Que desea realizar? 
        1. Gestion de Cruceros.
        2. Gestion de Habitaciones.
        3. Venta de Tours.
        4. Gestion de Restaurante.
        5. Estadísticas.
        6. Salir.
        > ''')
        while elección != "1" and elección != "2" and elección != "3" and elección != "4" and elección != "5" and elección != "6":
            elección = input(" Ingrese un numero válido [1,6]: ")

        # Numero "1" --> Gestion de Cruceros.
        if elección == '1':
            api = call_api()
            print_api(api)

        # Numero "2" --> Gestion de Habitaciones.
        elif elección == '2':

            try:
                cruices = pickle.load(open('Database_Cruceros.txt', 'rb'))
                clientes = pickle.load(open('Database_Clientes.txt', 'rb'))
            
                if cruices == None or clientes == None:
                    print("\n Todavía no hay ningún crucero o cliente en la base de datos.\n")

            except FileNotFoundError:
                api = call_api()
                cruices = build_cruisers(api)
                clientes = []

            while True:
            # ELECCIÓN que me permite saltar a la operación a realzar. 
                eleccion = input('''\n Bienvenido a la Gestion de Habitaciones Saman Caribbean 🛳️.
             \n ¿Que desea realizar? 
        1. Vender habitación.
        2. Desocupar habitación.
        3. Buscar habitación.
        4. Salir.
        > ''')
                while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4":
                    eleccion = input(" Ingrese un numero válido [1,4]: ")

                # Numero "1" --> Vende una habitación.
                if eleccion == '1':
                    clientes = leer_base_de_datos()
                    for i, cruice in enumerate(cruices, 1):
                        print('-'*4,str(i),'-'*28)
                        cruice.mostrar_name_of_cruices_and_route()
                    
                    option = input('\n Seleccione el numero correspondiente al crucero o ruta deseada: ')
                    while option != "1" and option != "2" and option != "3" and option != "4":
                        option = input(" Ingrese un numero válido [1,4]: ")

                    sell_room(cruices, clientes, option)
                    

                # Numero "2" --> Desocupa una habitación (sin borrar los datos del ocupante).
                elif eleccion == '2':
                    clientes = leer_base_de_datos()
                    for i, cruice in enumerate(cruices, 1):
                        print('-'*4,str(i),'-'*28)
                        cruice.mostrar_name_cruices()
                    
                    option = input('\n Seleccione el numero correspondiente al crucero para desocupar la habitación: ')
                    while option != "1" and option != "2" and option != "3" and option != "4":
                        option = input(" Ingrese un numero válido [1,4]: ")

                    cruices = desocupar_room(cruices, clientes, option)

                # Numero "3" --> Busca una habitación (tipo, capacidad, tipo+capacidad+numero).
                elif eleccion == '3':
                    for i, cruice in enumerate(cruices, 1):
                        print('-'*4,str(i),'-'*28)
                        cruice.mostrar_name_cruices()
                    
                    option = input('\n Seleccione el numero correspondiente al crucero para realizar la busqueda: ')
                    while option != "1" and option != "2" and option != "3" and option != "4":
                        option = input(" Ingrese un numero válido [1,4]: ")

                    busqueda = input('''\n Seleccione el tipo de busqueda que desea.
            1. Por tipo de habitación.
            2. Por capacidad.
            3. Por tipo y numero de habitación (A1).
            4. Salir.
            >''')
                    while busqueda != "1" and busqueda != "2" and busqueda != "3" and busqueda != "4":
                        busqueda = input(" Ingrese un numero válido [1,4]: ")

                    buscar_habitacion(cruices, clientes, option, busqueda)
                    

                # Numero "4" --> Rompe el ciclo y sale del programa.
                else:
                    pickle.dump(cruices, open('Database_Cruceros.txt', 'wb'))
                    pickle.dump(clientes, open('Database_Clientes.txt', 'wb'))
                    print('\n')
                    break
        


        # Numero "3" --> Venta de Tours.
        elif elección == '3':

            # Lee la base de datos, si no la encuentra crea la inicial.
            try:
                clientes = pickle.load(open('Database_Clientes_Tour.p', 'rb'))
                if clientes == None:
                        print("\n Todavía no hay ningún cliente en la base de datos.\n")
                else:
                    total_cupos = pickle.load(open('Database_Cupos.p', 'rb'))
                        
            except FileNotFoundError:
                total_cupos = {'El Dios de los Mares':{'en el puerto': 10, 'degustación de comida local': 100, 'trotar por el pueblo/ciudad': 0, 'visita a lugares históricos': 15}, 
                               'La Reina Isabel':{'en el puerto': 10, 'degustación de comida local': 100, 'trotar por el pueblo/ciudad': 0, 'visita a lugares históricos': 15}, 
                               'El Libertador del Océano':{'en el puerto': 10, 'degustación de comida local': 100, 'trotar por el pueblo/ciudad': 0, 'visita a lugares históricos': 15}, 
                               'Sabas Nieves':{'en el puerto': 10, 'degustación de comida local': 100, 'trotar por el pueblo/ciudad': 0, 'visita a lugares históricos': 15}}
                clientes = {}

            # ciclo que me permite repetir el código si se quiere seguir realizado cualquiera de las operaciones.
            while True:

                seguir = (input(" ¿Desea registar una compra de Saman Caribbean Tours 🛳️.? ('s' o 'n'): ")).lower()
                while seguir!='s' and seguir!='n':
                    seguir = (input(" Ingrese un carácter válido ('s' o 'n'): ")).lower()
                
                if seguir == 'n':
                    # Gurada las ventas realizadas en la base de datos
                    pickle.dump(clientes, open('Database_Clientes_Tour.p', 'wb'))
                    pickle.dump(total_cupos, open('Database_Cupos.p', 'wb'))
                    break
                
                else:
                    print('\n')
                    for i, crucero in enumerate(total_cupos):
                        print (f' {i+1}. {crucero}.')
                    option = input(' Ingrese el numero correspondiente a su crucero:')
                    while option != "1" and option != "2" and option != "3" and option != "4":
                        option = input(" Ingrese un numero válido [1,4]: ")
                    buy_tour(clientes, total_cupos, option)

        # Numero "4" --> Gestion de Restaurante.
        elif elección == '4':
            
            # ciclo que me permite repetir el cogió si se quiere seguir realizado cualquiera de las operaciones.
            while True:
                # ELECCIÓN que me permite saltar a la operación a realzar. 
                eleccion = input('''\n Bienvenido a la Gestion del Restaurante Saman Caribbean 🛳️.
                    \n ¿Que desea realizar? 
        1. Agregar un producto al Menú.
        2. Eliminar un producto del Menú.
        3. Modificar un producto del Menú.
        4. Agregar un combo al "Menu de Combos".
        5. Eliminar combo del "Menu de Combos".
        6. Buscar productos por nombre o rango de precio.
        7. Buscar combos por nombre o rango de precio.
        8. Salir.
        > ''')
                while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6" and eleccion != "7" and eleccion != "8":
                    eleccion = input(" Ingrese un numero válido [1,8]: ")

                # Numero "1" --> Agregar un producto al menú.
                if eleccion == '1':
                    food = identification_product()
                    print('\n')
                    print(food.mostrar_food_agregada())
                    
                # Numero "2" --> Eliminar un producto del menú.
                elif eleccion == '2':
                    print('\n')
                    if look_menu() == True:
                        while True:
                            option = (input('\n Clasificación Alimento "A" o Bebida "B": ')).upper()
                            while option != "A" and option != "B":
                                option = (input(' Ingreso inválido, ingrese una clasificación Alimento "A" o Bebida "B": ')).upper()
                            
                            number = input(" Ingrese el número correspondiente al producto que desea eliminar: ")
                            while not number.isnumeric():
                                number = input(" Ingreso invalido, ingrese el número correspondiente al producto que desea eliminar: ")
                            number = int(number)
                            
                            try:
                                print('\n')
                                delete_product_menu(option, number)
                                break
                            except (IndexError, UnboundLocalError):
                                    print("\n El número ingresado no corresponde a ningún producto, por favor intente otra vez.")


                # Numero "3" --> Modificar un producto del menú.
                elif eleccion == '3':
                    print("\n")
                    if look_menu() == True:
                        modificar = True
                        while modificar:
                            while True:
                                option = (input('\n Clasificación Alimento "A" o Bebida "B": ')).upper()
                                while option != "A" and option != "B":
                                    option = (input(' Ingreso inválido, ingrese una clasificación Alimento "A" o Bebida "B": ')).upper()
                            
                                number = input(" Ingrese el número correspondiente al producto que desea modificar: ")
                                while not number.isnumeric():
                                    number = input(" Ingreso invalido, ingrese el número correspondiente al producto que desea modificar: ")
                                number = int(number)
                                try:
                                    print("\n")
                                    update_product_menu(option, number)
                                    print("\n")
                                    modificar_info = input(" ¿Desea modificar la información de otro producto? ('S' para 'sí', 'N' para 'no'): ")
                                    while modificar_info.upper() != "S" and modificar_info.upper() != "N":
                                        modificar_info = input(" Ingreso inválido, ¿desea modificar la información de otro producto? ('S' para 'sí', 'N' para 'no'): ")
                                    if modificar_info.upper() == "S":
                                        continue
                                    elif modificar_info.upper() == "N":
                                        modificar = False
                                    break
                                except (IndexError, UnboundLocalError):
                                    print("\n")
                                    print(" El número ingresado no corresponde a ningún producto, por favor intente otra vez.")

                # Numero "4" --> Agregar un combo al "menu de combos".
                elif eleccion == '4':
                    combo = identification_combo()
                    print('\n')
                    print(combo.mostrar_combo())

                # Numero "5" --> Eliminar combo del "menu de combos".
                elif eleccion == '5':
                    print('\n')
                    if look_combos() == True:
                        while True:
                            number = input(" Ingrese el número correspondiente al combo que desea eliminar: ")
                            while not number.isnumeric():
                                number = input(" Ingreso invalido, ingrese el número correspondiente al combo que desea eliminar: ")
                            number = int(number)
                            
                            try:
                                print('\n')
                                delete_combo(number)
                                break
                            except (IndexError, UnboundLocalError):
                                    print("\n El número ingresado no corresponde a ningún combo, por favor intente otra vez.")

                # Numero "6" --> Buscar productos por nombre o rango de precio.
                elif eleccion == '6':
                    search_menu()

                # Numero "7" --> 7. Buscar combos por nombre o rango de precio.
                elif eleccion == '7':
                    search_combo()

                # Numero "8" --> Rompe el ciclo y sale del programa.
                else:
                    print("\n")
                    break

        # Numero "4" --> Estadísticas.    
        elif elección == '5':
             # ciclo que me permite repetir el cogió si se quiere seguir realizado cualquiera de las operaciones.
            while True:
                # ELECCIÓN que me permite saltar a la operación a realzar. 
                eleccion = input('''\n Bienvenido a la Gestion de Estadísticas Saman Caribbean 🛳️.
                    \n ¿Que desea realizar? 
        1. Promedio de gasto de un cliente en el crucero (Ticket + tours).
        2. Porcentaje de clientes que no compran tour.
        3. Top 3 clientes con mayor fidelidad en la línea.
        4. Top 3 cruceros con más ventas en tickets.
        5. Top 5 productos más vendidos en el restaurante.
        6. Salir.
        > ''')
                while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6":
                    eleccion = input(" Ingrese un numero válido [1,6]: ")

                if eleccion == '1':
                    pass
                elif eleccion == '2':
                    pass
                elif eleccion == '3':
                    pass
                elif eleccion == '4':
                    pass
                elif eleccion == '5':
                    api = call_api()
                    top_cinco_productos(api)
                else:
                    print('\n')
                    break
        # Numero "5" --> Rompe el ciclo y sale del programa.
        else:
            print('\n')
            break
    
    


main()