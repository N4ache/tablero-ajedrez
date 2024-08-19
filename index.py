#determinamos si es posible pintar un tablero del tamaño 'n x n' de manera que cada columna tenga una cantidad de celdas pintadas
def es_posible_pintar_tablero(n):
   
    #creamos un tablero de 'n x n' donde todas las celdas esten inicialmente en '0' 
    tablero = [[0 for _ in range(n)] for _ in range(n)]

    #pintamos el tablero pintando las primeras celdas de la fila con '1'
    for i in range(n):
        tablero[i][:i] = [1] * i
    
    #calculamos cuantas celdas pintadas hay en cada columna donde el resultado es una lista 'conteos_columnas'
    conteos_columnas = [sum(tablero[fila][col] for fila in range(n)) for col in range(n)]
    
    #verificamos que todos los valores de la lista son unicos, los elementos repetidos se eliminan
    if len(set(conteos_columnas)) != n:

        #si el numero de elementos unicos no coincide con 'n' devuelve 'false'
        return False
    
    #si todos los valores son unicos devuelve 'true'
    return True

#se prueban los dos tamaños de tablero pedidos (8x8 y 1000x1000) y se imprimen los resultados para ambos casos
n1 = 8
n2 = 1000
print(f"¿Es posible pintar un tablero de {n1}x{n1}?:", es_posible_pintar_tablero(n1))
print(f"¿Es posible pintar un tablero de {n2}x{n2}?:", es_posible_pintar_tablero(n2))
