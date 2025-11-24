# lab_booleanos.py
"""
Sesión 02: Tipos de Datos Básicos
Práctica: Booleanos (Boolean)

Objetivo: Implementar lógica de validación usando valores booleanos.
"""

def validar_producto(producto):
   """
   Valida si un producto cumple con los requisitos mínimos
   Args:
       producto (dict): Diccionario con datos del producto
   Returns:
       tuple: (bool, list) - (es_valido, lista_errores)
   """
   errores = []

   # Validar precio positivo
   if producto['precio'] > 0:
      precio_valido = True
   else:
        precio_valido = False
        errores.append("El precio debe ser positivo.")


   # Validar stock mínimo
   if producto ['stock'] > 0:
        stock_valido = True
   else:
       stock_valido = False
       errores.append("El stock debe ser mayor que cero.")


   # TODO: Validar nombre válido
   if producto ['nombre']:
       nombre_valido = True
   else:
          nombre_valido = False
          errores.append("El nombre no puede estar vacío.")


   # TODO: Validar categoría permitida
   categorias_permitidas = ['Computadoras', 'Electrónica', 'Ropa']
   if producto ['categoria'] in categorias_permitidas:
       categoria_valida= True
   else:
       categoria_valida = False
       errores.append("La categoría no es válida.")


   # Resultado final
   es_valido = precio_valido and stock_valido and nombre_valido and categoria_valida

   return (es_valido, errores)

def verificar_disponibilidad(producto):
   """
   Verifica si un producto está disponible para venta
   """
   # TODO: Implementar verificaciones
   en_stock = producto['stock'] > 0
   activo = producto['activo']
   precio_definido = producto['precio'] > 0

   return en_stock and activo and precio_definido

def main():
   # Productos de prueba
   productos = [
       {
           'nombre': 'Laptop HP',
           'precio': 1299.99,
           'stock': 5,
           'categoria': 'Computadoras',
           'activo': True
       },
       {
           'nombre': '',
           'precio': -50,
           'stock': 0,
           'categoria': 'Inválida',
           'activo': False
       }
   ]

   print("=== Sistema de Validación de Productos ===")

   for producto in productos:
       print(f"\nValidando producto: {producto['nombre']}")
       
       # Validar producto
       es_valido, errores = validar_producto(producto)
       
       if es_valido:
           print("✓ Producto válido")
           # Verificar disponibilidad
           disponible = verificar_disponibilidad(producto)
           print(f"Disponible para venta: {disponible}")
       else:
           print("✗ Producto inválido")
           for error in errores:
               print(f"  - {error}")

if __name__ == "__main__":
   main()

"""
Ejercicios adicionales:
1. Agregar validación de fecha de vencimiento
2. Implementar sistema de permisos de usuario
3. Validar restricciones de venta (edad, ubicación)
"""