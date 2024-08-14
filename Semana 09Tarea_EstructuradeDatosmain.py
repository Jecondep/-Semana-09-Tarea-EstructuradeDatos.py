
 # producto.py

class Producto:

  def _init_(self, id, nombre, cantidad, precio):
    self.id = id
    self.nombre = nombre
    self.cantidad = cantidad
    self.precio = precio  

  def getId(self):
    return self.id

  # Otros getters y setters


# inventario.py

class Inventario:

  def _init_(self):
    self.productos = []

  def agregar_producto(self, producto):
    self.productos.append(producto)

  def eliminar_producto(self, id):
    for producto in self.productos:
      if producto.id == id:
        self.productos.remove(producto)
        return
    print("Producto no encontrado")

  def actualizar_producto(self, id, detalles):
    # Lógica para actualizar detalles
    pass

  def buscar(self, nombre):
    # Devuelve productos que coincidan con el nombre
    pass

  def listar_productos(self):  
    for p in self.productos:
      print(p)


# main.py 

from inventario import Inventario  
from producto import Producto

inventario = Inventario()

# Agregar algunos productos de muestra
p1 = Producto(1, "Leche", 50, 10)   
inventario.agregar_producto(p1)

# Interfaz de usuario
while True:
  print("1. Agregar Producto")
  print("2. Eliminar Producto")
  # etc

  opcion = int(input())

  if opcion == 1:
     # Lógica para agregar producto

  elif opcion == 2:
     # Lógica para eliminar producto

  # etcnline Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
