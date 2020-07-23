from class_menu import Menu
class Combo(Menu):
    def __init__(self, name, total_price, products):
        Menu.__init__(self, name, total_price)
        self.products = products
    def mostrar_combo(self):
        return(f' Nombre: {self.name}\n Productos: '+(', '.join(self.products))+f'\n Precio: $ {self.total_price}')
        
    def mostrar_combo_menu(self):

        return(f' {self.name} | '+(self.products)+f' | ${self.total_price}')