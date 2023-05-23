# Sufriendo una y otra vez.
## Punto 1
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
## Punto 2
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
## Punto 3
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
## Punto 4
Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```python
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
```
## Punto 5
Desarrollar un programa que sume los elementos de una fila dada de una matriz.
```python
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
```
