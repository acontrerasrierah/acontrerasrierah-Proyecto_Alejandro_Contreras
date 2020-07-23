import requests

def call_api():
    """Llama al API, para recuperar la info.

    Returns:
        dic: info sobre los crucero.
    """
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    api = requests.get(url)
    return api.json()
def print_api(dic):
    """Imprime de manera ordenan la info del API.

    Args:
        dic (dic): info sobre los crucero.

    Returns:
        Un print de la info de cada crucero.
    """
    i = 0
    # Ciclo que permite ingresar en los cuatro tipos de cruceros, para imprimir su info.
    while i < 4:
        year, month, day = ((dic[i]['departure']).replace('-', '/').split('T')[0]).split('/')

        print(f''' \n Nombre del barco: {(dic[i]['name']).upper()}.\n
     Ruta: {" - ".join(dic[i]['route'])}
     Fecha de salida: {day}/{month}/{year}\n  
     Piso 1 -> Habitaciones Simples.
         Precio por habitación: ${dic[i]['cost']['simple']}.
         Capacidad de personas por habitación: {dic[i]['capacity']['simple']}.
         Cantidad de pasillo: {dic[i]['rooms']['simple'][1]}.
         Cantidad de habitaciones por pasillo: {dic[i]['rooms']['simple'][0]}.
         Total de habitaciones: {(dic[i]['rooms']['simple'][1])*(dic[i]['rooms']['simple'][0])}.\n
     Piso 2 -> Habitaciones Premium.
         Precio por habitación: ${dic[i]['cost']['premium']}.
         Capacidad de personas por habitación: {dic[i]['capacity']['premium']}.
         Cantidad de pasillo: {dic[i]['rooms']['premium'][1]}.
         Cantidad de habitaciones por pasillo: {dic[i]['rooms']['premium'][0]}.
         Total de habitaciones: {(dic[i]['rooms']['premium'][1])*(dic[i]['rooms']['premium'][0])}.\n
     Piso 3 -> Habitaciones VIP.
         Preciopor habitación: ${dic[i]['cost']['vip']}.
         Capacidad de personas por habitación: {dic[i]['capacity']['vip']}.
         Cantidad de pasillo: {dic[i]['rooms']['vip'][1]}.
         Cantidad de habitaciones por pasillo: {dic[i]['rooms']['vip'][0]}.
         Total de habitaciones: {(dic[i]['rooms']['vip'][1])*(dic[i]['rooms']['vip'][0])}.
     ''')
        i += 1
