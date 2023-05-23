def validar_matrices(matriz1, matriz2): #Valida si las matrices cumplen con las condiciones necesarias para realizar la operación.
    # Verificar si las matrices tienen la misma cantidad de filas y columnas
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return False #Si no cumplen las condiciones
    else:
        return True #Si cumplen las condiciones


def sumar_matrices(matriz1, matriz2): #Suma de dos matrices
    if validar_matrices(matriz1, matriz2):
        filas = len(matriz1)
        columnas = len(matriz1[0])
        matriz_suma = []

        for i in range(filas):
            fila = []
            for j in range(columnas):
                suma = matriz1[i][j] + matriz2[i][j]
                fila.append(suma)
            matriz_suma.append(fila)

        return matriz_suma #La matriz resultante de la suma
    else:
        return None #Si las matrices no cumplen las condiciones


def restar_matrices(matriz1, matriz2): #Resta de dos matrices
    if validar_matrices(matriz1, matriz2):
        filas = len(matriz1)
        columnas = len(matriz1[0])
        matriz_resta = []

        for i in range(filas):
            fila = []
            for j in range(columnas):
                resta = matriz1[i][j] - matriz2[i][j]
                fila.append(resta)
            matriz_resta.append(fila)

        return matriz_resta #La matriz resultante de la resta
    else:
        return None #Si las matrices no cumplen las condiciones


if __name__ == "__main__":
 #Ejemplos de matrices
 matriz1 = [[15, 27, 3],
           [48, 56, 6]]

 matriz2 = [[57, 888, 95],
           [105, 141, 152]]

# Realizar la suma de matrices
suma = sumar_matrices(matriz1, matriz2)

if suma is not None: #Si la matriz cumple las condiciones
    print("Suma de matrices:") #Imprimir el resultado
    for fila in suma:
        print(fila)
else:
    print("Las matrices no cumplen con las condiciones necesarias para la operación.") #Sino imprimir que no se cumple las condiciones

# Realizar la resta de matrices
resta = restar_matrices(matriz1, matriz2)

if resta is not None: #Si la matriz cumple las condiciones
    print("Resta de matrices:") #Imprimir el resultado
    for fila in resta:
        print(fila)
else:
    print("Las matrices no cumplen con las condiciones necesarias para la operación.") #Sino imprimir que no se cumple las condiciones
