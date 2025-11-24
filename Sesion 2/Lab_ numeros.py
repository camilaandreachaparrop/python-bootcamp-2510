# lab_numeros.py
"""
Sesión 02: Tipos de Datos Básicos
Práctica: Números Enteros (Integer)

Objetivo: Comprender y practicar el uso de números enteros en Python para análisis de datos.
"""

def calcular_inventario():
   """
   Simulación de sistema de inventario usando números enteros
   """
   # TODO: Define las variables de inventario
   productos_disponibles = 250 # Total de productos
   productos_vendidos = 10     # Productos vendidos hoy
   minimo_stock = 100          # Nivel mínimo permitido
   
   # TODO: Registra movimientos de inventario

   # 1. Añade 150 productos al inventario
   productos_disponibles += 150

   # 2. Registra venta de 45 productos
   productos_vendidos += 45
   productos_disponibles -= productos_vendidos
   
   # 3. Añade 25 productos más
   productos_disponibles += 25

   # 4. Calcula productos restantes
   productos_restantes = productos_disponibles



   # TODO: Realiza validaciones
   # 1. Verifica si el inventario está por debajo del mínimo (100)
   if productos_disponibles < minimo_stock:
    print (" El inventario está por debajo del mínimo permitido.")
   
   # 2. Calcula cuántos productos faltan para llegar al óptimo (200)
   stock_optimo = 200
   Productos_que_faltan= productos_restantes -stock_optimo
   
   return productos_disponibles

def main():
   """
   Función principal para ejecutar el programa
   """
   print("=== Sistema de Inventario ===")
   
   # Ejecutar cálculos
   total_productos = calcular_inventario()
   
   # Mostrar resultados
   print(f"Total en inventario: {total_productos}")

if __name__ == "__main__":
   main()

"""
Ejercicios adicionales:
1. Agregar validación de números negativos
2. Implementar contador de transacciones
3. Calcular valor total del inventario (precio unitario * cantidad)
"""