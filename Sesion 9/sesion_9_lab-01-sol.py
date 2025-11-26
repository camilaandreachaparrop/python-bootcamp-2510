"""
Laboratorio 1: Procesamiento de Archivo de Ventas
Objetivo: Practicar la lectura y escritura de archivos procesando un log de ventas

La función debe:
1. Leer un archivo de ventas con formato: fecha,producto,cantidad,precio
2. Calcular el total de ventas por producto
3. Generar un reporte con los resultados
"""

def procesar_ventas(archivo_entrada, archivo_salida):
    """
    Procesa un archivo de ventas y genera un reporte
    Args:
        archivo_entrada (str): Ruta del archivo de ventas
        archivo_salida (str): Ruta donde guardar el reporte
    Returns:
        dict: Resumen de ventas por producto
    Raises:
        NotImplementedError: Cuando el estudiante aún no implementa
        IOError: Cuando hay problemas con los archivos
    """
    # TODO: Implementar el procesamiento siguiendo estos pasos:
    # 1. Leer el archivo de ventas línea por línea
    with open(archivo_entrada, 'r') as f:
        lineas = f.readlines()
    # 2. Por cada línea:
    ventas = {}
    for linea in lineas:
    #    - Separar los campos (fecha,producto,cantidad,precio)
        fecha, producto, cantidad, precio = linea.strip().split(',')
        cantidad = int(cantidad)
        precio = float(precio)
    #    - Calcular el total (cantidad * precio)
        total = cantidad * precio
    #    - Acumular las ventas por producto
        if producto in ventas:
            ventas[producto] += total
        else:
            ventas[producto] = total
    # 3. Generar el reporte con los totales
    with open(archivo_salida, 'w') as f:
        f.write("Reporte de Ventas por Producto\n")
        f.write("-----------------------------\n")
        f.write("Ventas por Producto:\n")
        for producto, total in ventas.items():
            f.write(f"{producto}: ${total:.2f}\n")
        f.write("-----------------------------\n")
        f.write(f"Total de Ventas: ${sum(ventas.values()):.2f}\n")

def main():
    # Crear archivo de prueba
    datos_prueba = [
        "2024-02-01,Laptop,2,1200\n",
        "2024-02-01,Smartphone,1,800\n",
        "2024-02-02,Laptop,1,1200\n",
        "2024-02-02,Tablet,3,500\n"
    ]
    
    try:
        # Crear archivo de ventas
        with open("ventas.txt", "w") as archivo:
            archivo.writelines(datos_prueba)
        
        print("=== Procesamiento de Archivo de Ventas ===")
        print("\nContenido del archivo de ventas:")
        print("".join(datos_prueba))
        
        # Procesar ventas
        resultados = procesar_ventas("ventas.txt", "reporte_ventas.txt")
        
        print("\nReporte generado. Contenido:")
        with open("reporte_ventas.txt", "r") as archivo:
            print(archivo.read())
            
    except NotImplementedError as e:
        print(f"\nError: {str(e)}")
    except IOError as e:
        print(f"\nError de archivo: {str(e)}")

if __name__ == "__main__":
    main()