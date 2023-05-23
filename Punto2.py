def validar_matrices(matriz_a, matriz_b): #Se define la funcion
 #Valida las condiciones necesarias para realizar el producto de matrices.
 if len(matriz_a[0]) != len(matriz_b):  # Verificar que el número de columnas de la matriz A sea igual al número de filas de la matriz B
  return False
 if len(matriz_a) == 0 or len(matriz_b) == 0:   # Verificar que las matrices no estén vacías
  return False
    # Verificar que todas las filas de la matriz A tengan la misma longitud
 filas_a = len(matriz_a)
 longitud_fila_a = len(matriz_a[0])
 if not all(len(fila) == longitud_fila_a for fila in matriz_a):
  return False
    # Verificar que todas las filas de la matriz B tengan la misma longitud
 filas_b = len(matriz_b)
 longitud_fila_b = len(matriz_b[0])
 if not all(len(fila) == longitud_fila_b for fila in matriz_b):
        return False
    # Si todas las condiciones se cumplen, las matrices son válidas para la multiplicación
 return True


def multiplicar_matrices(matriz_a, matriz_b):
    #Realiza el producto de matrices. 
    filas_a = len(matriz_a)
    columnas_b = len(matriz_b[0])
    resultado = [[0] * columnas_b for _ in range(filas_a)]
    
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(len(matriz_b)):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    return resultado


if __name__ == "__main__": 
 #Ejemplo de matrices
 matriz_a = [[41, 562, 453],
            [456, 475, 654]]

 matriz_b = [[789, 843],
            [956, 10],
            [1561, 112]]

if validar_matrices(matriz_a, matriz_b): #Se hace la operacion si se cumple con las condiciones
    producto = multiplicar_matrices(matriz_a, matriz_b)
    print("El producto de matrices es:")
    for fila in producto:
        print(fila)
else:
    print("Las matrices no cumplen las condiciones necesarias para realizar el producto.") #Sino se imprime que no se cumple las condiciones
