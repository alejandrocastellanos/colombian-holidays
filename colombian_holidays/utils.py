"""
Utilidades para cálculos de fechas y festivos.
"""

from datetime import datetime, timedelta


def calculate_easter(year: int) -> datetime:
    """
    Calcular el Domingo de Pascua usando el algoritmo de Meeus/Jones/Butcher.

    Args:
        year: El año para calcular la Pascua

    Returns:
        datetime representando el Domingo de Pascua
    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    return datetime(year, month, day)


def move_to_monday(date: datetime) -> datetime:
    """
    Mover una fecha al lunes siguiente según la Ley Emiliani.

    Args:
        date: La fecha original

    Returns:
        La fecha movida al lunes siguiente si no es lunes
    """
    if date.weekday() == 0:
        return date

    days_until_monday = (7 - date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7

    return date + timedelta(days=days_until_monday)
