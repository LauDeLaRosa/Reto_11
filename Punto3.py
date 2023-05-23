def validar_matriz(matriz):
    #Valida las condiciones necesarias para obtener la matriz transpuesta.
    if len(matriz) == 0: # Verificar que la matriz no esté vacía
        return False
    filas = len(matriz)  # Verificar que todas las filas tengan la misma longitud
    longitud_fila = len(matriz[0])
    if not all(len(fila) == longitud_fila for fila in matriz):
        return False
    # Si todas las condiciones se cumplen, la matriz es válida para obtener la matriz transpuesta
    return True


def obtener_transpuesta(matriz): #Se define para obtener la matriz transpuesta 
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0] * filas for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    
    return transpuesta


if __name__ == "__main__": 
 #Ejemplos de matriz
 matriz = [[145, 234, 345],
          [4687, 532, 456]]

if validar_matriz(matriz): #Si se cumple con las condiciones se realiza el proceso
    transpuesta = obtener_transpuesta(matriz)
    print("La matriz transpuesta es:")
    for fila in transpuesta:
        print(fila)
else:
    print("La matriz no cumple las condiciones necesarias para obtener la transpuesta.") #Sino se imprime que no se cumplen las condiciones
