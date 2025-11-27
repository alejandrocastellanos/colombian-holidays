"""
Colombian Holidays
==================

Una librería Python para verificar días festivos en Colombia.
Incluye soporte para la Ley Emiliani y todos los domingos como festivos.
"""

from .colombian_holidays import (
    ColombianHolidays,
    is_today_holiday,
    get_today_holiday_name,
    is_holiday,
    get_holiday_name,
    list_holidays,
)

__version__ = "1.0.0"
__author__ = "Tu Nombre"
__all__ = [
    "ColombianHolidays",
    "is_today_holiday",
    "get_today_holiday_name",
    "is_holiday",
    "get_holiday_name",
    "list_holidays",
]
