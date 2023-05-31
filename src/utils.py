from datetime import datetime


def save_movement(deposit):
    movement = (0, datetime.now(), 0)
    movements = [movement]

    # Agregar un movimiento
    last_movement = movements[-1]
    balance = last_movement[2] + deposit
    movement = (deposit, datetime.now(), balance)
    movements.append(movement)

    # Imprimir todos los movimientos
    for movement in movements:
        print(f"Monto: {movement[0]}, Fecha: {movement[1]}, Saldo: {movement[2]}")


def get_printstatement():
    print("Hi")