# fecha - date
# monto - amount
# saldo - balance
# nombre - nameUser
# numero de cuenta - account number
# comportamiento - se muestre los movimientos
# ((ingreso, retiro(-))amount y (saldo(balance)=+-)
# fecha se muestre DD/MM/AAAA
# lista -

"""pizza.append(ingredientes)
from datetime import datetime
now = datetime.now()"""

Date = ["DD/MM/AAA"]
Amount = [200]

account = [Date], [Amount]
print("movimiento", account)


def ask_deposit():
    account_deposit = input("Ingresa un monto para depositar: ")
    if account_deposit.isdigit() and int(account_deposit) > 0:
        print(f'El monto es {account_deposit}. ¡El monto que ingresaste es válido!')
        return int(account_deposit)
    else:
        print("El monto que ingresaste es inválido. Debes ingresar un monto válido")


ask_deposit()


def ask_withdraw():
    account_withdraw = input("Ingresa un monto para retirar: ")
    if account_withdraw.isdigit() and int(account_withdraw) > 0:
        print(f'El monto a retirar {account_withdraw}. ¡El monto a retirar que ingresaste es válido!')
        return int(account_withdraw)
    else:
        print("El monto a retirar que ingresaste es inválido. Debes ingresar un monto válido")


ask_withdraw()
