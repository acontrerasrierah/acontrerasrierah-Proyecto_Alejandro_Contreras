import matplotlib.pylot as plt

def promedio_gasto():
    pass

def porcentaje_no_tour():
    pass

def tres_mejores_clientes():
    pass

def top_tres_cruceros():
    pass

def top_cinco_productos(api):

    for i, cruceros in enumerate(api, 1):
        print('-'*4,str(i),'Crucero.' ,'-'*21)
        print(' ',cruceros['name'].title())
    print('-'*37)

    option = input('\n Seleccione el numero correspondiente al crucero deseado: ')
    while option != "1" and option != "2" and option != "3" and option != "4":
        option = input(" Ingrese un numero válido [1,4]: ")
    option = int(option) - 1
    
    crucero = api[option]

    best_sellers = []
    for product in crucero['sells']:
        food = [product['name'], product['price'], product['amount']]
        best_sellers.append(food)

    sorted_list = sorted(best_sellers, key=lambda l: l[2], reverse = True)
    for i, lista in enumerate(sorted_list, 1):
        print('-'*4,str(i)+'°. '+'-'*28)
        print(f' Nombre del producto: {lista[0]}.\n Precio: ${lista[1]}.\n Cantidad vendida: {lista[2]}.')

def graficos():
    pass

