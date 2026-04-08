import random
import os
import time
import math


# Distancia Manhattan: útil para movimientos en 4 direcciones
def distancia_manhattan(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


# Distancia Euclidiana: útil para medir cercanía general en 8 direcciones
def distancia_euclidiana(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)


# Crea el tablero y coloca al ratón, al gato y la salida
def crear_tablero(ancho, alto, posicion_raton, posicion_gato, salida):
    tablero = [[" . " for _ in range(ancho)] for _ in range(alto)]

    rx, ry = posicion_raton
    gx, gy = posicion_gato
    sx, sy = salida

    tablero[sy][sx] = "🏁"
    tablero[ry][rx] = "🐭"
    tablero[gy][gx] = "😼"

    return tablero


# Mueve una pieza si la nueva posición está dentro del tablero
def mover(posicion, movimiento, ancho, alto):
    x, y = posicion
    dx, dy = movimiento

    nx = x + dx
    ny = y + dy

    if 0 <= nx < ancho and 0 <= ny < alto:
        return (nx, ny)
    return (x, y)


# Limpia la consola y muestra el tablero actual
def mostrar_tablero(tablero, turno):
    os.system("cls" if os.name == "nt" else "clear")

    print(f"Turno {turno}\n")

    for fila in tablero:
        print("".join(fila))
    print()


# Heurística del ratón:
# - premia llegar a la salida
# - castiga ser atrapado
# - intenta acercarse a la salida sin quedar demasiado cerca del gato
def evaluar_raton(posicion_raton, posicion_gato, salida):
    if posicion_raton == posicion_gato:
        return -1000
    if posicion_raton == salida:
        return 10000

    distancia_salida = distancia_manhattan(posicion_raton, salida)
    distancia_gato = distancia_euclidiana(posicion_raton, posicion_gato)

    return -distancia_salida + 0.1 * distancia_gato


# Heurística del gato:
# - premia atrapar al ratón
# - busca acercarse lo máximo posible
def evaluar_gato(posicion_raton, posicion_gato):
    if posicion_raton == posicion_gato:
        return -1000

    distancia_raton = distancia_euclidiana(posicion_raton, posicion_gato)
    return 10 * distancia_raton


# Algoritmo Minimax:
# - maximizando=True  -> turno del ratón
# - maximizando=False -> turno del gato
def minimax(
    posicion_raton,
    posicion_gato,
    salida,
    profundidad,
    maximizando,
    movimientos_posibles_raton,
    movimientos_posibles_gato,
    ancho,
    alto
):
    # Caso base: profundidad agotada o juego terminado
    if profundidad == 0 or posicion_raton == posicion_gato or posicion_raton == salida:
        if maximizando:
            return evaluar_raton(posicion_raton, posicion_gato, salida)
        else:
            return evaluar_gato(posicion_raton, posicion_gato)

    if maximizando:
        # Turno del ratón: busca el mayor valor posible
        mejor_valor = -float("inf")

        for movimiento in movimientos_posibles_raton:
            nueva_posicion_raton = mover(posicion_raton, movimiento, ancho, alto)
            valor = minimax(
                nueva_posicion_raton,
                posicion_gato,
                salida,
                profundidad - 1,
                False,
                movimientos_posibles_raton,
                movimientos_posibles_gato,
                ancho,
                alto
            )
            mejor_valor = max(mejor_valor, valor)

        return mejor_valor

    else:
        # Turno del gato: busca el menor valor para perjudicar al ratón
        peor_valor = float("inf")

        for movimiento in movimientos_posibles_gato:
            nueva_posicion_gato = mover(posicion_gato, movimiento, ancho, alto)
            valor = minimax(
                posicion_raton,
                nueva_posicion_gato,
                salida,
                profundidad - 1,
                True,
                movimientos_posibles_raton,
                movimientos_posibles_gato,
                ancho,
                alto
            )
            peor_valor = min(peor_valor, valor)

        return peor_valor


# Elige el mejor movimiento posible para el ratón
def elegir_movimiento_raton(
    posicion_raton,
    posicion_gato,
    salida,
    profundidad,
    movimientos_posibles_raton,
    movimientos_posibles_gato,
    ancho,
    alto
):
    mejor_valor = -float("inf")
    mejor_movimiento = None

    for movimiento in movimientos_posibles_raton:
        nueva_posicion_raton = mover(posicion_raton, movimiento, ancho, alto)
        valor = minimax(
            nueva_posicion_raton,
            posicion_gato,
            salida,
            profundidad,
            False,
            movimientos_posibles_raton,
            movimientos_posibles_gato,
            ancho,
            alto
        )

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento


# Elige el mejor movimiento posible para el gato
def elegir_movimiento_gato(
    posicion_gato,
    posicion_raton,
    salida,
    profundidad,
    movimientos_posibles_raton,
    movimientos_posibles_gato,
    ancho,
    alto
):
    mejor_valor = float("inf")
    mejor_movimiento = None

    for movimiento in movimientos_posibles_gato:
        nueva_posicion_gato = mover(posicion_gato, movimiento, ancho, alto)
        valor = minimax(
            posicion_raton,
            nueva_posicion_gato,
            salida,
            profundidad,
            True,
            movimientos_posibles_raton,
            movimientos_posibles_gato,
            ancho,
            alto
        )

        if valor < mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento

    return mejor_movimiento


def main():
    ancho = 13
    alto = 13

    # Posiciones iniciales
    raton = (3, 3)
    gato = (9, 9)
    salida = (12, 12)

    # El ratón se mueve en 4 direcciones
    movimientos_posibles_raton = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    # El gato se mueve en 8 direcciones
    movimientos_posibles_gato = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    turno = 1

    # Simulación principal
    while raton != salida and gato != raton and turno <= 50:
        tablero = crear_tablero(ancho, alto, raton, gato, salida)
        mostrar_tablero(tablero, turno)

        # Primeros turnos del ratón aleatorios, luego usa minimax
        if turno <= 5:
            movimiento_raton = random.choice(movimientos_posibles_raton)
        else:
            movimiento_raton = elegir_movimiento_raton(
                raton,
                gato,
                salida,
                3,
                movimientos_posibles_raton,
                movimientos_posibles_gato,
                ancho,
                alto
            )
        raton = mover(raton, movimiento_raton, ancho, alto)

        # Primeros turnos del gato aleatorios, luego usa minimax
        if turno <= 20:
            movimiento_gato = random.choice(movimientos_posibles_gato)
        else:
            movimiento_gato = elegir_movimiento_gato(
                gato,
                raton,
                salida,
                5,
                movimientos_posibles_raton,
                movimientos_posibles_gato,
                ancho,
                alto
            )
        gato = mover(gato, movimiento_gato, ancho, alto)

        time.sleep(1)
        turno += 1

    # Estado final
    tablero = crear_tablero(ancho, alto, raton, gato, salida)
    mostrar_tablero(tablero, turno)

    if turno > 50:
        print("Empate técnico")
    elif raton == salida:
        print("¡El ratón escapó!")
    else:
        print("¡El gato atrapó al ratón!")

    print("Simulación finalizada ✅")


if __name__ == "__main__":
    main()