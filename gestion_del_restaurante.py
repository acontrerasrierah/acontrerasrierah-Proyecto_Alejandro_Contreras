from class_food import Food
from class_combo import Combo

def add_product_menu(name, option):
    """
    Esta función toma por teclado los datos de un nuevo producto para agregarlo a la base de datos del menu ('Database_Menu_Alimentos.txt' o 'Database_Menu_Bebidas.txt').

    Argumentos => name: nombre del producto ingresado por teclado.
                  option: clasificación del producto ('Alimento' o 'Bebida').

    Retorna => Registro del nuevo producto en el archivo .txt correspondiente, notificación de registro exitoso y retorno de objeto 'Food' con la información recibida.

    """
    while True:
        price = input(' Precio del producto: ').replace(',','.')
        try:
            float(price)
        except ValueError:
            print (' Introduzca un valor numérico.')
        else:
            price = float(price)
            if price <= 0:
                print (' Introduzca un numero mayor a 0.')
            else:
                break
    total_price = price + (price*0.16)

    if option == 'A':
        elección = input(' Alimento de Empaque "E" o Preparación "P": ' )
        while (elección.upper() != "E") and (elección.upper() != "P"):
            elección = input(' Ingreso inválido, alimento de Empaque "E" o Preparación "P": ')
        if elección == 'E':
            extra = 'Empaque'
        else:
            extra = 'Preparación'
        food = Food(name, total_price, extra, tipo = 'Alimento')
        with open('Database_Menu_Alimentos.txt', 'a+') as dbma:
            dbma.write(f'{food.tipo}//{food.name}//{food.extra}//{food.total_price}\n')
        print(f' El alimento: "{name}" fue agregado exitosamente al Menu.\n')

    else:
        elección = input(' Tamaño de la bebida Grande "G", Mediana "M" o Pequeña "P": ')
        while (elección.upper() != "G") and (elección.upper() != "M") and (elección.upper() != "P"):
            elección = input(' Ingreso inválido, tamaño de la bebida Grande "G", Mediana "M" o Pequeña "P": ')
        if elección == 'G':
            extra = 'Grande'
        elif elección == 'M':
            extra = 'Mediana'
        else:
            extra = 'Pequeña'
        food = Food(name, total_price, extra, tipo = 'Bebida')
        with open('Database_Menu_Bebidas.txt', 'a+') as dbmb:
            dbmb.write(f'{food.tipo}//{food.name}//{food.extra}//{food.total_price}\n')
        print(f' La bebida: "{name}" fue agregada exitosamente al Menu.\n')
    
    return food

def identification_product():
    """
    Esta función toma por teclado el name y option del producto. Si se encuentra en la base de datos, no pide más información. Si no está, se ejecuta la función add_product_menu(name, option). Si no hay ningún producto registrado, lo notifica e igualmente ejecuta la función add_product_menu(name, option).

    Argumentos => n/a

    Retorna =>
    \tSi está en la lista: objeto 'Food' con la información correspondiente al producto ya existente.
    \tSi no está en la lista: retorna el producto de la ejecución de la función 'add_product_menu(name, option)'
    \tSi el archivo .txt no existe o no hay nadie registrado: retorna el producto de la ejecución de la función 'add_product_menu(name, option)' después de notificar la inexistencia de productos registrados.
    
    """
    option = (input('\n Clasificación Alimento "A" o Bebida "B": ')).upper()
    while option != "A" and option != "B":
        option = (input(' Ingreso inválido, ingrese una clasificación Alimento "A" o Bebida "B": ')).upper()
                            
    name = input('\n Nombre del Alimento/Bedida: ')
    while not ("".join(name.split(" "))).isalpha():
        name = input(" Ingreso inválido, ingrese el nombre del Alimento/Bedida:  ")

    try:
        if option == 'A':
            with open("Database_Menu_Alimentos.txt") as dbma:
                datos = dbma.readlines()
            for dato in datos:
                producto = dato[:-1].split("//")
                if producto[1] == name:
                    print("\n Producto ya registrado.")
                    food = Food(producto[1],producto[3],producto[2],producto[0])
                    return food
                else:
                    return add_product_menu(name, option)
        
        elif option == 'B':
            with open("Database_Menu_Bebidas.txt") as dbmb:
                datos = dbmb.readlines()
            for dato in datos:
                producto = dato[:-1].split("//")
                if producto[1] == name:
                    print("\n Producto ya registrado.")
                    food = Food(producto[1],producto[3],producto[2],producto[0])
                    return food
                else:
                    return add_product_menu(name, option)

    except FileNotFoundError:
        print("\n Todavía no hay ningún producto en el menu.")
        return add_product_menu(name, option)

def delete_product_menu(option, number):
    """
    Se recorre la base de datos de productos registrados ('Database_Menu_Alimentos.txt' o 'Database_Menu_Bebidas.txt') y se elimina el deseado.

    Argumentos => option: clasificación del producto ('Alimento' o 'Bebida').
                  number: número asignado previamente al producto que se desea eliminar.

    Retorna => Eliminación del producto elegido del archivo .txt, notificación de que el producto fue eliminado y ejecución de la función look_menu() después de eliminarlo.

    """
    if option == 'A':
        with open("Database_Menu_Alimentos.txt") as dbma:
            datos = dbma.readlines()
            for dato in datos:
                producto = dato[:-1].split("//")
                eliminar = datos[number-1]
                producto_eliminado = eliminar[:-1].split("//")
        with open("Database_Menu_Alimentos.txt", "w") as dbma:
            for dato in datos:
                if dato != eliminar:
                    dbma.write(dato)

    else:
        with open("Database_Menu_Bebidas.txt") as dbmb:
            datos = dbmb.readlines()
            for dato in datos:
                producto = dato[:-1].split("//")
                eliminar = datos[number-1]
                producto_eliminado = eliminar[:-1].split("//")
        with open("Database_Menu_Bebidas.txt", "w") as dbmb:
            for dato in datos:
                if dato != eliminar:
                    dbmb.write(dato)

    print ("\n Producto "+producto_eliminado[1]+" eliminado de la base de datos.\n")
    look_menu()

        
def update_product_menu(option, number):
    """
    Esta función permite modificar la información previamente almacenada en la base de datos de los productos ('Database_Menu_Alimentos.txt' o 'Database_Menu_Bebidas.txt').

    Argumentos => option: clasificación del producto ('Alimento' o 'Bebida').
                  number: número asignado previamente al producto que se desea eliminar.

    Retorna => Modificación del archivo .txt, notificación de modificación exitosa y ejecución del método mostrar_food_agregada() sobre el objeto 'food'.

    """
    if option == 'A':
        with open("Database_Menu_Alimentos.txt") as dbma:
            datos = dbma.readlines()
        for i, dato in enumerate(datos):
            if i == (number-1):
                producto = dato[:-1].split("//")
                food = Food(producto[1],producto[3],producto[2],producto[0])

    else:
        with open("Database_Menu_Bebidas.txt") as dbmb:
            datos = dbmb.readlines()
        for i, dato in enumerate(datos):
            if i == (number-1):
                producto = dato[:-1].split("//")
                food = Food(producto[1],producto[3],producto[2],producto[0])
        


    print(f" 1. Nombre del Producto: {food.name}\n 2. Detalle: {food.extra}\n 3. Precio: {food.total_price}")
    atributo = input("\n Ingrese el número correspondiente a la especificación que desea modificar: ")
    while (not atributo.isnumeric()) or (int(atributo) not in range(1,5)):
        atributo = input(f" Ingreso inválido, ingrese el número correspondiente al especificación que desea modificar: ")
    
    if atributo == "1":
        food.name = input('\n Nuevo nombre del producto: ')
        while not ("".join(food.name.split(" "))).isalpha():
            food.name = input(" Ingreso inválido, ingrese el nuevo nombre del producto: ")
        producto[1] = food.name

    elif atributo == "2":
        if option == 'A':
            elección = input(' Alimento de Empaque "E" o Preparación "P": ' )
            while (elección.upper() != "E") and (elección.upper() != "P"):
                elección = input(' Ingreso inválido, alimento de Empaque "E" o Preparación "P": ')
            if elección == 'E':
                food.extra = 'Empaque'
            else:
                food.extra = 'Preparación'

        else:
            elección = input('\n Nuevo tamaño de la bebida Grande "G", Mediana "M" o Pequeña "P": ')
            while (elección.upper() != "G") and (elección.upper() != "M") and (elección.upper() != "P"):
                elección = input(' Ingreso inválido, nuevo tamaño de la bebida Grande "G", Mediana "M" o Pequeña "P": ')
            if elección == 'G':
                food.extra = 'Grande'
            elif elección == 'M':
                food.extra = 'Mediana'
            else:
                food.extra = 'Pequeña'

        producto[2] = food.extra

    else:
        while True:
            price = input(' Precio nuevo del producto: ').replace(',','.')
            try:
                float(price)
            except ValueError:
                print (' Introduzca un valor numérico.')
            else:
                price = float(price)
                if price <= 0:
                    print (' Introduzca un numero mayor a 0.')
                else:
                    break

        food.total_price = price + (price*0.16)
        producto[3] = food.total_price

    if option == 'A':
        with open("Database_Menu_Alimentos.txt") as dbma:
            datos = dbma.readlines()
        for i in range(len(datos)):
            if i == (number-1):
                datos[number-1] = f'{food.tipo}//{food.name}//{food.extra}//{food.total_price}\n'
        with open("Database_Menu_Alimentos.txt", 'w') as dbma:
            dbma.writelines(datos)

    else:
        with open("Database_Menu_Bebidas.txt") as dbmb:
            datos = dbmb.readlines()
        for i in range(len(datos)):
            if i == (number-1):
                datos[number-1] = f'{food.tipo}//{food.name}//{food.extra}//{food.total_price}\n'
        with open("Database_Menu_Bebidas.txt", 'w') as dbmb:
            dbmb.writelines(datos)

    print("\n\t\t Producto modificado con éxito.\n")
    print(food.mostrar_food_agregada())

def add_combo(name):
    """
    Esta función toma por teclado los datos de un nuevo combo para agregarlo a la base de datos del menu de combos ('Database_Menu_Combos.txt').

    Argumentos => name: nombre del combo ingresado por teclado.

    Retorna => Registro del nuevo combo en el archivo .txt correspondiente, notificación de registro exitoso y retorno de objeto 'Combo' con la información recibida.

    """
    while True:
        price = input(' Precio del combo: ').replace(',','.')
        try:
            float(price)
        except ValueError:
            print (' Introduzca un valor numérico.')
        else:
            price = float(price)
            if price <= 0:
                print (' Introduzca un numero mayor a 0.')
            else:
                break
    total_price = price + (price*0.16)

    products = []
    aux = 0
    while True:
        aux += 1

        product = input(f' Nombre del {aux}.º producto: ')
        while not ("".join(name.split(" "))).isalpha():
            product = input(" Ingreso inválido, ingrese el nombre del producto:  ")
        products.append(product)

        seguir = (input(" ¿Desea ingresar otro producto? ('s' o 'n'): ")).lower()
        while seguir!='s' and seguir!='n':
            seguir = (input(" Ingrese un carácter válido ('s' o 'n'): ")).lower()
        if seguir == 'n':
            break
        else:
            continue

    if aux <= 2:
        print(' Es necesario un minimo de 2 productos para crear un combo')
    else:
        combo = Combo(name, total_price, products)
        with open('Database_Menu_Combos.txt', 'a+') as dbmc:
            dbmc.write(f'{combo.name}//{combo.products}//{combo.total_price}\n')
            # '+(', '.join(food.products))+'
        print(f' El combo: "{name}" fue agregada exitosamente al "Menu de Combos".')
        print('\n')
        return combo

def identification_combo():
    """
    Esta función toma por teclado el name del combo. Si se encuentra en la base de datos, no pide más información. Si no está, se ejecuta la función add_combo(name). Si no hay ningún combo registrado, lo notifica e igualmente ejecuta la función add_combo(name).

    Argumentos => n/a

    Retorna =>
    \tSi está en la lista: objeto 'Combo' con la información correspondiente al producto ya existente.
    \tSi no está en la lista: retorna el producto de la ejecución de la función 'add_combo(name)'
    \tSi el archivo .txt no existe o no hay nadie registrado: retorna el combo de la ejecución de la función 'add_combo(name)' después de notificar la inexistencia del combo registrados.
    
    """
    name = input('\n Nombre del combo: ')
    while not ("".join(name.split(" "))).isalpha():
        name = input(" Ingreso inválido, ingrese el nombre del combo:  ")

    try:
        with open("Database_Menu_Combos.txt") as dbmc:
            datos = dbmc.readlines()
        for dato in datos:
            combo_aux = dato[:-1].split("//")
            if combo_aux[0] == name:
                print("\n Combo ya registrado.")
                combo = Combo(combo_aux[0],combo_aux[1],combo_aux[2])
                return combo
        else:
            return add_combo(name)
    except FileNotFoundError:
        print("\n Todavía no hay ningún combo en el Menu de Combos.")
        return add_combo(name)

def delete_combo(number):
    """
    Se recorre la base de datos de combos registrados ('Database_Menu_Combos.txt') y se elimina el deseado.

    Argumentos => number: número asignado previamente al combo que se desea eliminar.

    Retorna => Eliminación del combo elegido del archivo .txt, notificación de que el combo fue eliminado y ejecución de la función look_combos() después de eliminarlo.

    """
    with open("Database_Menu_Combos.txt") as dbmc:
        datos = dbmc.readlines()
        eliminar = datos[number-1]
        combo_eliminado = eliminar[:-1].split('//')
    with open("Database_Menu_Combos.txt", "w") as dbmc:
        for dato in datos:
            if dato != eliminar:
                dbmc.write(dato)
    
    print(f'\n\t\t El combo "{combo_eliminado[0]}" fue eliminado del Menu de Combos.\n')
    look_combos()

def search_menu():
    """
    Esta función toma los datos de los productos en la base de datos del menu ('Database_Menu_Alimentos.txt' o 'Database_Menu_Bebidas.txt'). 
    Luego toma por teclado el tipo de busqueda (1 -> Nombre y 2 -> Rango) y dependiendo de la busqueda seleccionada ordena el menu. 
    Si selecciona "Nombre" ejecutar la función search_product(sorted_menu, product).
    Si selecciona "Rango" pregunta por los rangos.

    Argumentos => n/a.

    Retorna => Si selecciona "1 -> Nombre" retorna una impresión del producto buscado con sus datos.
               Si selecciona "2 -> Rango" retorna una impresión de los productos dentro del rango.

    """
    alimentos = []
    bebidas = []
    
    with open("Database_Menu_Alimentos.txt") as dbma:
        datos = dbma.readlines()
    if len(datos) == 0:
        print("\n Todavía no hay ningún alimento en el menu.\n")
    else:
        for dato in datos:
            producto = dato[:-1].split("//")
            producto_aux = producto[1],producto[3],producto[2],producto[0]
            alimentos.append(producto_aux)
        
    with open("Database_Menu_Bebidas.txt") as dbmb:
        datos = dbmb.readlines()
    if len(datos) == 0:
        print("\n Todavía no hay ninguna bebida en el Menu.\n")
    else:
        for dato in datos:
            producto = dato[:-1].split("//")
            producto_aux = producto[1],producto[3],producto[2],producto[0]
            bebidas.append(producto_aux)

    while True:
        option = input('''\n Desea realizar la búsqueda por:\n
     1. Nombre.
     2. Rango.
     3. Salir.
     > ''')
        while option != "1" and option != "2" and option != "3":
            option = input(" Ingrese un numero válido [1,3]: ")

        if option == '1':
            elección = (input(" ¿Desea buscar un Alimento o una Bebida? ('a' o 'b'): ")).lower()
            while elección!='a' and elección!='b':
                elección = (input(" Ingrese un carácter válido ('a' o 'b'): ")).lower()
            name = input(' Nombre del producto a buscar: ')
            while not ("".join(name.split(" "))).isalpha():
                name = input(" Ingreso inválido, ingrese el nombre del producto a buscar: ")
            
            if elección == 'a':
                sorted_list = sorted(alimentos, key=lambda l: l[0])
            else:
                sorted_list = sorted(bebidas, key=lambda l: l[0])
            product_found = search_product(sorted_list, name)
            print(f'\n Nombre de Producto: {product_found[0]}\n Clasificación: {product_found[3]}\n Detalle: {product_found[2]}\n Precio: ${product_found[1]}\n')
        
        elif option == '2':
            sorted_menu_alimentos = sorted(alimentos, key=lambda l: l[1])
            sorted_menu_bebidas = sorted(bebidas, key=lambda l: l[1])

            while True:
                max_price = input('\n Precio maximo del producto: ').replace(',','.')
                try:
                    float(max_price)
                except ValueError:
                    print (' Introduzca un valor numérico.')
                else:
                    max_price = float(max_price)
                    if max_price <= 0:
                        print (' Introduzca un numero mayor a 0.')
                    else:
                        break 
            
            while True:
                minimun_price = input(' Precio minimo del producto: ').replace(',','.')
                try:
                    float(minimun_price)
                except ValueError:
                    print (' Introduzca un valor numérico.')
                else:
                    minimun_price = float(minimun_price)
                    if minimun_price <= 0:
                        print (' Introduzca un numero mayor a 0.')
                    else:
                        break

            print ('\n\t \tMENU\n ALIMENTOS:')
            for lista in sorted_menu_alimentos:
                aux = float(lista[1])
                if aux < float(max_price) and aux > float(minimun_price):
                    print(f' {lista[0]} | {lista[2]} | ${lista[1]}')   
            print ('\n BEBIDAS:')
            for lista in sorted_menu_bebidas:
                aux = float(lista[1])
                if aux < float(max_price) and aux > float(minimun_price):
                    print(f' {lista[0]} | {lista[2]} | ${lista[1]}')   
            print ('\n')
        else:
            print("\n")
            break

def search_combo():
    """
    Esta función toma los datos de los combos en la base de datos del menu de combos ('Database_Menu_Combos.txt'). 
    Luego toma por teclado el tipo de busqueda (1 -> Nombre y 2 -> Rango) y dependiendo de la busqueda seleccionada ordena el menu de combos. 
    Si selecciona "Nombre" ejecutar la función search_product(sorted_menu, product).
    Si selecciona "Rango" pregunta por los rangos.

    Argumentos => n/a.

    Retorna => Si selecciona "1 -> Nombre" retorna una impresión del combo buscado con sus datos.
               Si selecciona "2 -> Rango" retorna una impresión de los combos dentro del rango.

    """
    
    combos = []
    with open("Database_Menu_Combos.txt") as dbmc:
        datos = dbmc.readlines()
    if len(datos) == 0:
        print("\n Todavía no hay ningún alimento en el menu.\n")
    else:
        for dato in datos:
            producto = dato[:-1].split("//")
            producto_aux = producto[0],producto[1],producto[2]
            combos.append(producto_aux)
    
    while True:
        option = input(''' Desea realizar la búsqueda por:\n 
     1. Nombre.
     2. Rango.
     3. Salir.
     > ''')
        while option != "1" and option != "2" and option != "3":
            option = input(" Ingrese un numero válido [1,3]: ")

        if option == '1':
            product = input('\n Nombre del combo a buscar: ')
            while not ("".join(product.split(" "))).isalpha():
                product = input(" Ingreso inválido, ingrese el nombre del combo a buscar: ")
            
            sorted_menu = sorted(combos, key=lambda l: l[0])
            product_found = search_product(sorted_menu, product)
            print(f' {product_found[0]} | {product_found[1]} | ${product_found[2]}')

        elif option == '2':
            sorted_menu = sorted(combos, key=lambda l: l[2])
            print(sorted_menu)

            while True:
                max_price = input('\n Precio maximo del producto: ').replace(',','.')
                try:
                    float(max_price)
                except ValueError:
                    print (' Introduzca un valor numérico.')
                else:
                    max_price = float(max_price)
                    if max_price <= 0:
                        print (' Introduzca un numero mayor a 0.')
                    else:
                        break 
            
            while True:
                minimun_price = input(' Precio minimo del producto: ').replace(',','.')
                try:
                    float(minimun_price)
                except ValueError:
                    print (' Introduzca un valor numérico.')
                else:
                    minimun_price = float(minimun_price)
                    if minimun_price <= 0:
                        print (' Introduzca un numero mayor a 0.')
                    else:
                        break

            print ('\n\t \tMENU DE COMBOS')
            for lista in sorted_menu:
                aux = float(lista[2])
                if aux < float(max_price) and aux > float(minimun_price):
                    print(f' {lista[0]} | {lista[1]} | ${lista[2]}')   
            print ('\n')
                
        else:
            print("\n")
            break

def look_menu():
    """
    Esta función muestra la información de todos los productos previamente almacenados en la base de datos del menu.

    Argumentos => n/a

    Retorna => 
    \tSi hay productos registrados: imprime los productos numerados por clasificación.
    \tSi el archivo .txt no existe o no hay producto registrado: notifica que no existen productos registrados.

    """
    alimentos = []
    bebidas = []
    try:
        with open("Database_Menu_Alimentos.txt") as dbma:
            datos = dbma.readlines()
        if len(datos) == 0:
            print("\n Todavía no hay ningún alimento en el menu.\n")
        else:
            for dato in datos:
                producto = dato[:-1].split("//")
                alimentos.append(Food(producto[1],producto[3],producto[2],producto[0]))
            print("\n\t\t MENU\n ALIMENTOS: ")
            for i, alimento in enumerate(alimentos):
                print('-'*2,str(i+1),'-'*18)
                print(alimento.mostrar_food_menu())
            
            
        with open("Database_Menu_Bebidas.txt") as dbmb:
            datos = dbmb.readlines()
        if len(datos) == 0:
            print("\n Todavía no hay ninguna bebida en el Menu.\n")
        else:
            for dato in datos:
                producto = dato[:-1].split("//")
                bebidas.append(Food(producto[1],producto[3],producto[2],producto[0]))
            print("\n BEBIDAS: ")
            for i, bebida in enumerate(bebidas):
                print('-'*2,str(i+1),'-'*18)
                print(bebida.mostrar_food_menu())
            return True

    except FileNotFoundError:
        print("\n Todavía no hay ningún producto en el Menu.\n")
        return False

def look_combos():
    """
    Esta función muestra la información de todos los combos previamente almacenados en la base de datos del menu de combos.

    Argumentos => n/a

    Retorna => 
    \tSi hay productos combos: imprime los combos numerados.
    \tSi el archivo .txt no existe o no hay combos registrados: notifica que no existen combos registrados.

    """
    combos = []
    try:
        with open("Database_Menu_Combos.txt") as dbmc:
            datos = dbmc.readlines()
        if len(datos) == 0:
            print("\n Todavía no hay ningún alimento en el Menu de Combos.\n")
        else:
            for dato in datos:
                combo = dato[:-1].split("//")
                combos.append(Combo(combo[0],combo[2],combo[1]))
            print("\n\t\t MENU\n COMBOS: ")
            for i, combo_aux in enumerate(combos):
                print('-'*2,str(i+1),'-'*18)
                print(combo_aux.mostrar_combo_menu())
            return True

    except FileNotFoundError:
        print("\n Todavía no hay ningún producto en el Menu de Combos.\n")
        return False

def search_product(sorted_menu, product):
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

