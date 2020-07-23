from class_menu import Menu

class Food(Menu):
    def __init__(self, name, total_price, extra, tipo):
        Menu.__init__(self, name, total_price)
        self.extra = extra
        self.tipo = tipo

    def mostrar_food_agregada(self):
        if (self.tipo) == 'Alimento':
            return(f' {self.tipo} de {self.extra}\n Nombre: {self.name}.\n Precio: {self.total_price}')
        else:
            return(f' {self.tipo}\n Nombre: {self.name}.\n Tamaño: {self.extra}.\n Precio: {self.total_price}')

    def mostrar_food_menu(self):
        return(f' {self.name}. | {self.extra} | Precio: {self.total_price}')
