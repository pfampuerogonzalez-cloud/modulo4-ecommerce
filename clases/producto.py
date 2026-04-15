class Producto:
  def __init__(self, id, nombre, categoria, precio ):
      self.id = id
      self.nombre = nombre
      self.categoria = categoria
      self.precio = precio

  def __str__(self):
      return f"el id del producto es: {self.id} - el nombre del producto es: {self.nombre} - su categoria es: {self.categoria} - su precio es: {self.precio}"
  
