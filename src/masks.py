"""Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
7000792289606361# входной аргумент
7000 79** **** 6361# выход функции"""

CARD = "7000792289606361"
ACCOUNT = "73654108430135878845"


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты в виде строки и возвращает
    её маску в формате XXXX XX** **** XXXX."""

    card_number = card_number.replace(" ", "")

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked = card_number[:6] + "******" + card_number[-4:]

    return f"Номер карты: {masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


print(get_mask_card_number(CARD))


"""Функция get_mask_account принимает на вход номер счета и возвращает его маску.
Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:
73654108430135878845  # входной аргумент
**4305  # выход функции"""


def get_mask_account(account_number: str) -> str:
    """Принимает номер карты в виде строки и возвращает
    её маску в формате **XXXX."""
    account_number = account_number.replace(" ", "")
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен состоять из 16 цифр")

    masked = "**" + account_number[-4:]

    return f"Номер счета:  {masked}"


print(get_mask_account(ACCOUNT))
