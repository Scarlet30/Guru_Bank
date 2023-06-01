from src.data import ask_deposit, ask_withdraw
from src.utils import save_movement

options = 0

while options != 4:

    options = int(input("Que quieres hacer? \n 1. Deposito \n 2. Retiro \n 3. Ver extracto \n 4. Salir \n"))

    if options == 1:
        save_movement(ask_deposit())

    elif options == 2:
        save_movement(ask_withdraw())

    elif options == 3:
        print("opcion3")

    else:
        print("No elegiste una opción.")

print("Saliste")