# Clases Utilizadas
from class_room import Room
from class_cruise import Cruise
from class_dato_del_cliente import Datos_del_Cliente

# Librerías utilizadas. Se utilizo math para aproximar una division hacia arriba y pickle para leer y escribir un archivo.
import math
import pickle

def build_cruisers(api):
    """

    Bajo la lectura del API, genera la lista de cruceros con sus respectivos datos.

    """
    cruisers = []
    for cruiser in api:
        name = cruiser['name']
        route = cruiser['route']
        departure = cruiser['departure']
        costs = cruiser['cost']
        capacities = cruiser['capacity']
        simple_halls = cruiser['rooms']['simple'][1]
        simple_rooms_per_hall = cruiser['rooms']['simple'][0]
        premium_halls = cruiser['rooms']['premium'][1]
        premium_rooms_per_hall = cruiser['rooms']['premium'][0]
        vip_halls = cruiser['rooms']['vip'][1]
        vip_rooms_per_hall = cruiser['rooms']['vip'][0]
        simple_rooms = build_rooms(simple_halls, simple_rooms_per_hall, 'simple')
        premium_rooms = build_rooms(premium_halls, premium_rooms_per_hall, 'premium')
        vip_rooms = build_rooms(vip_halls, vip_rooms_per_hall, 'vip')
        total_rooms = simple_rooms + premium_rooms + vip_rooms
        cruiser = Cruise(name, route, departure, capacities, total_rooms, costs)
        cruisers.append(cruiser)
    
    return cruisers

def build_rooms(halls_count, rooms_per_hall, room_type):
    """

    Genera la enumeración de las habitaciones en base a la cantidad de pasillos y habitaciones por pasillos.

    """
    rooms = []
    for i in range(0, halls_count):
        hall_id = chr(ord('A') + i)
        for j in range(0, rooms_per_hall):
            room_id = str(j + 1)
            rooms.append(Room(room_id, hall_id, room_type))

    return rooms

def sell_room(cruices, clientes, option):
    """

    Vende las habitaciones con respecto a el tipo de habitación seleccionado y la cantidad de personas.

    """
    option = int(option)
    eleccion = input('''\n Seleccione el tipo de habitación:
        1. Simple.
        2. Premium.
        3. VIP.
        > ''')
    while eleccion != "1" and eleccion != "2" and eleccion != "3":
        eleccion = input(" Ingrese un numero válido [1,3]: ")
    
    if eleccion == '1':
        aux = 'simple'
    elif eleccion == '2':
        aux = 'premium'
    else:
        aux = 'vip'

    personas = input(' Cantidad de personas: ')
    while not personas.isnumeric() or int(personas)<0:
        personas = input(' Cantidad de personas: ')
    personas = int(personas)
    cruise = cruices[option-1]
    habitaciones = cruise.mostrar_habitaciones_disponibles(aux)
    room_price = cruise.costs[aux]
    rooms_capacity = cruise.capacities[aux]
    minimum_rooms = math.ceil(personas / rooms_capacity) 
    print(' Debe escoger como minimo', minimum_rooms, 'habitaciones')
    if minimum_rooms > len(habitaciones):
        print(f' Error, no hay suficientes habitaciones {aux} disponibles')
        return
    rooms_requested = input(' Escriba las habitaciones que quiera, separadas por espacio: ')
    rooms_requested = rooms_requested.strip().split(' ')
    
    while not set(rooms_requested).issubset(set(habitaciones)) or len(set(rooms_requested)) > personas or len(set(rooms_requested)) < minimum_rooms:
        if len(rooms_requested) > personas:
            print(' No puede escoger mas habitaciones que personas. Por favor intente de nuevo. ')
        if len(rooms_requested) < minimum_rooms:
            print(' Debe escoger como minimo', minimum_rooms, 'habitaciones')
        rooms_requested = input(' Escriba las habitaciones que quiera, separadas por espacio: ')
        rooms_requested = rooms_requested.strip().split(' ')
    
    people_remaining = personas
    total_price = 0
    for i, room in enumerate(rooms_requested):
        valid = False
        while not valid:
            people_for_room = input(' Ingrese la cantidad de personas que quiere para la habitacion %s: ' %(room))
            while not people_for_room.isnumeric():
                people_for_room = input(' Ingrese la cantidad de personas que quiere para la habitacion', room, ': ')
            try:
                assert 0 < int(people_for_room) <= rooms_capacity
                assert (people_remaining - int(people_for_room)) // rooms_capacity + 1 <= (len(rooms_requested) - i)
                if personas == rooms_capacity:
                    assert int(people_for_room) == rooms_capacity
                    people_for_room = int(people_for_room)
                    valid = True
                else:
                    people_for_room = int(people_for_room)
                    valid = True
            except:
                if 0 < int(people_for_room) <= rooms_capacity:
                    print(' Debe ingresar mas gente en esta habitacion.')
                elif (people_remaining - int(people_for_room)) // rooms_capacity + 1 <= (len(rooms_requested) - i):
                    print(' Debe ingresar menos gente en esta habitacion para ocupar todas las habitaciones que pidió.')
                else:
                    print(' Debe ingresar mas gente en esta habitacion.')
                    

        people_remaining -= people_for_room
        clientes_aux = pedir_datos(clientes, people_for_room, room_price, room, aux)
        total_price += imprimir_factura(room, room_price, aux, clientes_aux)
    print('-'*2,'EL MONTO TOTAL POR LA/LAS HABITACIÓN/HABITACIONES','-'*4,'\n\t','$'*5,total_price,'$'*5)
    cruices = marcar_habitaciones_seleccionadas(cruices, clientes_aux, option, aux)
    pickle.dump(cruices, open('Database_Cruceros.txt', 'wb'))
    pickle.dump(clientes, open('Database_Clientes.txt', 'wb'))
    return clientes, cruices
    

def pedir_datos(clientes, people_for_room, room_price, room, aux):
    """

    Pregunta y guarda los datos del cliente tipo objeto 'Dato_del_Cliente'.

    """
    while people_for_room != 0:
        nombre = input('\n Nombre completo: ')
        while not ("".join(nombre.split(" "))).isalpha():
            nombre = input(" Ingreso inválido, ingrese nombre:  ")
        while True:
            dni = input(' DNI: ').replace('.','')
            try:
                int(dni)
            except ValueError:
                print (' Introduzca un valor numérico.')
            else:
                if len(dni) < 6:
                    print (' DNI tiene como minimo 6 números.') 
                else:
                    break
        if numero_primo(dni) and numero_abundante(dni):
            descuento = 0.25
        elif numero_primo(dni):
            descuento = 0.10
        elif numero_abundante(dni):
            descuento = 0.15
        else:
            descuento = 0
        
        edad = input(" Edad (entre 5 y 110): ")
        while not edad.isnumeric():
            edad = input(" Ingreso inválido, ingrese la edad (entre 5 y 110): ")
        edad = int(edad)
        while (edad < 0) or (edad > 110):
            edad = input(" Ingreso inválido, ingrese la edad (entre 5 y 110): ")
            while not edad.isnumeric():
                edad = input(" Ingreso inválido, ingrese su edad (entre 5 y 110): ")
            edad = int(edad)
        # if edad >= 65 and aux == 'simple':
        #     # TODO: chequiar esto
        #     aux == 'premium'
        
        discapacidad = input(' Discapacidad (s/n):')
        while discapacidad.upper() != "S" and discapacidad.upper() != "N":
            discapacidad = input(' Ingreso invalido, ingrese discapacidad (s/n):')
        dinero = room_price + (room_price*descuento)
        clientes.append(Datos_del_Cliente(nombre, dni, descuento, edad, discapacidad, aux, room, dinero))
        
        people_for_room -= 1
    return clientes

def numero_primo(dni):
    """

    Verifica si el DNI es un numero primo

    """
    dni = int(dni)
    for x in range(2, dni):
        if dni%x == 0:
            return False
    return True

def numero_abundante(dni):
    """

    Verifica si el DNI es un numero abundante

    """
    dni = int(dni)
    factores = [f for f in range(1, dni) if dni%f == 0]
    suma = sum(factores)
    return suma > dni

def leer_base_de_datos():
    """

    Lee la base de datos de los clientes, si no existe enviá un mesaje y crea una base.

    """
    try:
        clientes = pickle.load(open('Database_Clientes.p', 'rb'))
        if clientes == None:
            clientes = []
            print("\n Todavía no hay ningún cliente en la base de datos.\n")
            return clientes

    except FileNotFoundError:
        clientes = []
        return clientes

def marcar_habitaciones_seleccionadas(cruices, clientes_aux, option, aux):
    """

    Agrega el dni a las habitacion seleccionadas por el usuario, convirtiendolas en habitaciones ocupadas.

    """
    cruise = cruices[option-1]
    rooms = [f for f in cruise.rooms if f.room_type == aux]
    for room in rooms:
        for cliente in clientes_aux:
            hall_aux, room_number = list(cliente.habitacion)
            occupant_dni = cliente.dni
            if (hall_aux, room_number) == (room.hall, room.id):
                room.occupant_dni = occupant_dni
    rooms_aux = [f for f in cruise.rooms if f.room_type != aux]
    total_rooms = rooms + rooms_aux
    cruices[option-1].rooms = total_rooms
    return cruices

def desocupar_room(cruices, clientes, option):

    option = int(option)
    eleccion = input('''\n Seleccione el tipo de habitación:
        1. Simple.
        2. Premium.
        3. VIP.
        > ''')
    while eleccion != "1" and eleccion != "2" and eleccion != "3":
        eleccion = input(" Ingrese un numero válido [1,3]: ")
    
    if eleccion == '1':
        aux = 'simple'
    elif eleccion == '2':
        aux = 'premium'
    else:
        aux = 'vip'
    
    cruise = cruices[option-1]
    # rooms = [f for f in cruise.rooms if f.room_type == aux and f.occupant_dni == dni]
    cruise.mostrar_habitaciones_no_disponibles(aux)

    while True:
        dni = input(' Ingrese el dni de la persona: ').replace('.', '')
        try:
            int(dni)
        except ValueError:
            print (' Introduzca un valor numérico.')
        else:
            if len(dni) < 6:
                print (' DNI tiene como minimo 6 números.') 
            rooms = [f for f in cruise.rooms if f.room_type == aux and f.occupant_dni == dni]
            if rooms == None:
                print(' Ingrese el dni de la otra persona registrada en la habitacion.')
            else:
                break
    cruices = habilitar_habitaciones_seleccionadas(cruices, clientes, option, aux, dni)

    return cruices

def habilitar_habitaciones_seleccionadas(cruices, clientes, option, aux, dni):
    """

    Agrega el dni a las habitacion seleccionadas por el usuario, convirtiendolas en habitaciones ocupadas.

    """
    cruise = cruices[option-1]
    rooms = [f for f in cruise.rooms if f.room_type == aux]
    for room in rooms:
        for cliente in clientes:
            hall_aux, room_number = list(cliente.habitacion)
            # occupant_dni = cliente.dni
            if (hall_aux, room_number) == (room.hall, room.id):
                room.occupant_dni = None
    rooms_aux = [f for f in cruise.rooms if f.room_type != aux]
    total_rooms = rooms + rooms_aux
    cruices[option-1].rooms = total_rooms

    return cruices

def imprimir_factura(room, room_price, aux, clientes_aux):


    print('-'*4,'FACTURA DE LA HABITACIÓN ',room, aux.upper(),'-'*4)
    price = 0
    for i, cliente in enumerate(clientes_aux, 1):
        print('-'*4,i, ' CLIENTE','-'*18)
        price += cliente.dinero
        if cliente.discapacidad == 's':
            discapacidad = "si"
        else:
             discapacidad = "no"
        print(f' Nombre completo: {cliente.nombre}.\n DNI: {cliente.dni}.\n Edad: {cliente.edad}.\n Descuento: {cliente.descuento*100}%\n Discapacidad: {discapacidad}.\n Precio del ticket: ${room_price}.\n Pecio con descuento includo: ${cliente.dinero}.')
    print('-'*4,'PRECIO POR LA HABITAION ', room,'-'*6)
    print(f' Total sin IVA: ${price}\n TOTAL CON IVA: ${price+(price*0.16)}\n')
    return (price+(price*0.16))


def search_product(sorted, product):
    """
    Esta función muestra es la implementación de un binary search, para buscar el producto dentro de sorted_menu.

    Argumentos => sorted_menu = menu ordenado por nombre.
                  product = nombre del producto.

    Retorna => 
    \tSi producto esta sorted_menu: retorna dicho producto.
    \tSi producto no esta sorted_menu: retorna una impresión que no se encontró el producto.

    """
    left, right = 0, len(sorted_menu)-1
    if left <= right:
        if len(sorted_menu) == 0:
            return print ('Error, lista vaciá.')
        mid = len(sorted_menu) // 2
        if sorted_menu[mid][0] == product:
            return sorted_menu[mid]
        if sorted_menu[mid][0] < product:
            return search_product(sorted_menu[mid+1:], product)
        elif sorted_menu[mid][0] > product:
            return search_product(sorted_menu[:mid], product)
    return print (f'\n No se encontró "{product}" en el menu.')
