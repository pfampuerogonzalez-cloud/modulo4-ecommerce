from producto import Producto


class Catalogo:
    def __init__(self):
        self.productos = []
    
    #def __str__(self):
        #return f"{self.productos}"
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_catalogo(self):
        for producto in self.productos:
            print(producto)

    def eliminar_producto(self, id ):
        pass

        


p = Producto(1,"computador", "tecnologia", 1000000)
catalogo = Catalogo()
catalogo.agregar_producto(p)
catalogo.agregar_producto(p)
catalogo.agregar_producto(p)
catalogo.agregar_producto(p)
catalogo.listar_catalogo()

