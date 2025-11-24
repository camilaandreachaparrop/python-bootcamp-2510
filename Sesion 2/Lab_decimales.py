# lab_decimales.py
"""
Sesión 02: Tipos de Datos Básicos
Práctica: Números Decimales (Float)

Objetivo: Practicar operaciones con números decimales en un contexto de análisis de precios.
"""

def calcular_precio_final(precio_base, cantidad):
   """
   Calcula el precio final de una venta incluyendo impuestos y descuentos
   Args:
       precio_base (float): Precio unitario del producto
       cantidad (int): Cantidad de unidades
   Returns:
       tuple: (subtotal, impuestos, descuento, total)
   """
   # Constantes
   IVA = 0.19  # 19% IVA
   DESCUENTO_MAYOR = 0.10  # 10% descuento por compra mayor
   LIMITE_DESCUENTO = 1000.0  # Límite para aplicar descuento
   
   # TODO: Calcular subtotal (precio_base * cantidad)
   subtotal = precio_base * cantidad
      
   # TODO: Calcular impuestos (subtotal * IVA)
   impuestos = subtotal * IVA
     
   # TODO: Calcular descuento si subtotal > LIMITE_DESCUENTO
   if subtotal > LIMITE_DESCUENTO:
      descuento = subtotal * DESCUENTO_MAYOR
   else:
       descuento = 0.0 
   
   # TODO: Calcular total final (subtotal + impuestos - descuento)
   total = subtotal + impuestos - descuento
   
   return (subtotal, impuestos, descuento, total)

def formatear_precio(valor):
   """
   Da formato a un valor numérico como precio
   Args:
       valor (float): Cantidad a formatear
   Returns:
       str: Valor formateado como precio
   """
   # TODO: Implementar formato de dos decimales
   return f"${valor:,.2f}"

def main():
   # Datos de prueba
   productos = [
       {"nombre": "Laptop", "precio": 1299.99, "cantidad": 2},
       {"nombre": "Mouse", "precio": 24.50, "cantidad": 5},
       {"nombre": "Teclado", "precio": 99.99, "cantidad": 3}
   ]
   
   print("=== Sistema de Precios ===")
   
   # TODO: Procesar cada producto
   for producto in productos:
       # Calcular precios
       subtotal, impuestos, descuento, total = calcular_precio_final(
           producto['precio'], 
           producto['cantidad']
       )
       
       # Mostrar resultados
       print(f"\nProducto: {producto['nombre']}")
       print(f"Subtotal: {formatear_precio(subtotal)}")
       print(f"Impuestos: {formatear_precio(impuestos)}")
       print(f"Descuento: {formatear_precio(descuento)}")
       print(f"Total: {formatear_precio(total)}")

if __name__ == "__main__":
   main()

"""
Ejercicios adicionales:
1. Implementar descuentos por temporada
2. Calcular precio promedio por unidad
3. Encontrar el producto más costoso
"""