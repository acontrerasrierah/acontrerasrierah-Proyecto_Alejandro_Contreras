class Cruise():
    def __init__(self, name, route, departure, capacities, rooms = [], costs = {}):
        self.name = name
        self.route = route
        self.departure = departure
        self.capacities = capacities
        self.rooms = rooms
        self.costs = costs

    def mostrar_name_of_cruices_and_route(self):

        print(f' Nombre del Crucero: {self.name}')
        print(f' Ruta: '+' - '.join(self.route)+'')

    def mostrar_habitaciones_disponibles(self, aux):
        numeros = []
        for i, room in enumerate(self.rooms):
            if room.occupant_dni == None and room.room_type == aux:
                numeros.append(room.hall+room.id)

        print('\n')
        for i in range(0, len(numeros), 4):
            print(' ', numeros[i:i+4])      
        print('\n')
        return numeros
 
    def mostrar_name_cruices(self):
    
        print(f' Nombre del Crucero: {self.name}')

    def mostrar_habitaciones_no_disponibles(self, aux):
        numeros = []
        for i, room in enumerate(self.rooms):
            if room.occupant_dni != None and room.room_type == aux:
                numeros.append(room.hall+room.id)

        print('\n')
        for i in range(0, len(numeros), 4):
            print(' ', numeros[i:i+4])      
        print('\n')
        