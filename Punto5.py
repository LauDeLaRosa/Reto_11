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


def sumar_fila(matriz, fila): #Se define la funcion para la suma de la fila
    # Verificar si la fila está dentro del rango válido
    if fila < 0 or fila >= len(matriz):
        return None
    
    suma = sum(matriz[fila])
    return suma


if __name__ == "__main__": 
 matriz = [[461, 5652, 4543],
          [334354, 5453, 6554],
          [357, 353358, 59]]

fila_deseada = 2  # Ejemplo de la fila deseada

if validar_matriz(matriz):
    resultado = sumar_fila(matriz, fila_deseada)
    if resultado is not None:
        print(f"La suma de la fila {fila_deseada} es: {resultado}") #Si la matriz cumple las condiciones se resuelve
    else:
        print(f"La fila {fila_deseada} está fuera del rango válido.")
else:
    print("La matriz no cumple las condiciones necesarias.") #Sino no se hace
