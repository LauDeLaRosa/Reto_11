def validar_matriz(matriz):# Se define la funcion para validar las condiciones de la matriz
    # Verificar que la matriz no esté vacía
    if len(matriz) == 0:
        return False
    # Verificar que todas las filas tengan la misma longitud
    filas = len(matriz)
    longitud_fila = len(matriz[0])
    if not all(len(fila) == longitud_fila for fila in matriz):
        return False
    # Si todas las condiciones se cumplen, la matriz es válida para operar
    return True


def sumar_columna(matriz, columna): #Se define la funcion que suma una columna de la matriz
    # Verificar si la columna está dentro del rango válido
    if columna < 0 or columna >= len(matriz[0]):
        return None
    
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    
    return suma


if __name__ == "__main__": 
 #Ejemplo de matriz
 matriz = [[14, 2324, 553],
          [456, 4555, 566],
          [897, 8764, 5649]]

columna_deseada = 1  # Sumar la columna 1 (segunda columna)

if validar_matriz(matriz):
    resultado = sumar_columna(matriz, columna_deseada)
    if resultado is not None:
        print(f"La suma de la columna {columna_deseada} es: {resultado}") #Se opera si la matriz cumple las condiciones
    else:
        print(f"La columna {columna_deseada} está fuera del rango válido.") 
else:
    print("La matriz no cumple las condiciones necesarias.") #Sino, no se opera
