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

    def buscar_por_id(self):
         for in p in self.productos:
            if p.id == id:
                print(p)
                return p

    def eliminar_producto(self, id):
        buscar = self.buscar_por_id(id)
        self.productos.remove(p)

    def guardar_catalogo(self, nombre_archivo="catalogo.txt"):
        try
            with open(nombre_archivo,"w") as f:
                for p in self.productos:
                    f.write(f"{p.id},{p.nombre},{p.categoria},{p.precio}\n")
        except Exception as error:
            print(f"error en el archivo: {error}")



tupla = ()
tupla.

        
