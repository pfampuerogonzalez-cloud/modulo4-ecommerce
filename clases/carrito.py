class Carrito:
    def __init__(self):
        self. items = {}

    def __str__(self):
        return f"{self.items}"
    
    def agregar(self, producto, cantidad):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def ver_carrito(self):
        total=0
        for p,c in self.items():
            subtotal = p.precio * c
            total += subtotal 
            print(f"{p.nombre} - cantidad{c} - subtotal {subtotal}")
        print(f"total de la compra: {total}")


    def total(self):
        pass

    def vaciar(self):
        self.vaciar(clear)



p1 = Carrito()
p2 = Carrito()
p3 = Carrito()
p4 = Carrito()

carrito = Carrito()
carrito.agregar(p1,2)
carrito.agregar(p2,2)
carrito.agregar(p3,2)
carrito.agregar(p4,2)

