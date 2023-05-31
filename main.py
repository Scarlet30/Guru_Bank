from src.data import ask_deposit, ask_withdraw
from src.utils import get_printStatement


options = {
    '1': ('Deposit', ask_deposit()),
    '2': ('withdraw', ask_withdraw()),
    '3': ('Statement', get_printStatement)
}
