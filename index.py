def es_posible_pintar_tablero(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        tablero[i][:i] = [1] * i
    
    conteos_columnas = [sum(tablero[fila][col] for fila in range(n)) for col in range(n)]
    
    if len(set(conteos_columnas)) != n:
        return False
    
    return True

n1 = 8
n2 = 1000
print(f"¿Es posible pintar un tablero de {n1}x{n1}?:", es_posible_pintar_tablero(n1))
print(f"¿Es posible pintar un tablero de {n2}x{n2}?:", es_posible_pintar_tablero(n2))
