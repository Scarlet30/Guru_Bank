from src.data import ask_deposit
from src.utils import save_movement


options = int(input("Que quieres hacer? \n 1. Deposito \n 2. Retiro \n 3. Ver extracto \n"))

if options == 1:
    save_movement(ask_deposit())

elif options == 2:
    print("opcion2")

elif options == 3:
    print("opcion3")

else:
    print("No elegiste una opción.")
