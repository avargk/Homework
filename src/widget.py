from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета, сохраняя тип"""
    parts = info_string.split()
    number = parts[-1]
    name_of = " ".join(parts[:-1])
    if not info_string or not isinstance(info_string, str):
        return "Некорректный ввод: строка пуста"
    if len(parts) > 3:
        return "Некорректный ввод: лишние данные"

    if name_of.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{name_of} {mask_number}"


print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """ Принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ.
    Использует модуль datetime для обработки любых корректных строк
    """
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return "Некорректный формат даты"


print(get_date("2024-03-11T02:26:18.671407"))
