from masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета, сохраняя тип"""
    parts = info_string.split()
    number = parts[-1]
    name_of = " ".join(parts[:-1])

    if name_of.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{name_of} {mask_number}"


print(mask_account_card("MasterCard 7158300734726758"))


def get_date(date_string: str) -> str:
    """Принимает строку с датой и временем, возвращает дату в формате ДД.ММ.ГГГГ."""
    year = date_string[0:4]  # '2003'
    month = date_string[5:7]  # '11'
    day = date_string[8:10]  # '21'

    return f"{day}.{month}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))
