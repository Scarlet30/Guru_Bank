
def ask_deposit():
    account_deposit = input("Ingresa un monto para depositar: ")
    if account_deposit.isdigit() and int(account_deposit) > 0:
        print(f'El monto es {account_deposit}. ¡El monto que ingresaste es válido!')
        return int(account_deposit)

    else:
        print("El monto que ingresaste es inválido. Debes ingresar un monto válido")


def ask_withdraw():
    account_withdraw = input("Ingresa un monto para retirar: ")
    if account_withdraw.isdigit() and int(account_withdraw) > 0:
        print(f'El monto a retirar {account_withdraw}. ¡El monto a retirar que ingresaste es válido!')
        return int(account_withdraw)
    else:
        print("El monto a retirar que ingresaste es inválido. Debes ingresar un monto válido")
