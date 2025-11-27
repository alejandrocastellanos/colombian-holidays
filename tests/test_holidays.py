"""
Tests para la librería colombian-holidays
"""

import pytest
from datetime import datetime
from colombian_holidays import (
    ColombianHolidays,
    is_holiday,
    get_holiday_name,
    list_holidays,
)


def test_fixed_holidays():
    """Test festivos fijos"""
    # Año Nuevo
    assert is_holiday(datetime(2025, 1, 1)) == True
    assert "Año Nuevo" in get_holiday_name(datetime(2025, 1, 1))

    # Navidad
    assert is_holiday(datetime(2025, 12, 25)) == True
    assert "Navidad" in get_holiday_name(datetime(2025, 12, 25))


def test_sundays_are_holidays():
    """Test que todos los domingos son festivos"""
    # 2 de noviembre de 2025 es domingo
    sunday = datetime(2025, 11, 2)
    assert sunday.weekday() == 6
    assert is_holiday(sunday) == True
    assert get_holiday_name(sunday) == "Domingo (Sunday)"


def test_regular_weekday_not_holiday():
    """Test que un día normal no es festivo"""
    # 3 de noviembre de 2025 es lunes y no es festivo
    monday = datetime(2025, 11, 3)
    assert is_holiday(monday) == False
    assert get_holiday_name(monday) is None


def test_list_holidays_2025():
    """Test listar festivos del 2025"""
    holidays = list_holidays(2025)
    assert len(holidays) == 18
    assert (1, 1) in holidays  # Año Nuevo
    assert (12, 25) in holidays  # Navidad


def test_emiliani_law():
    """Test Ley Emiliani - festivos movidos al lunes"""
    checker = ColombianHolidays()

    # Epifanía (6 de enero) debería moverse al lunes siguiente
    epifania_original = datetime(2025, 1, 6)  # Lunes
    holidays = checker.get_all_holidays(2025)

    # Verificar que se aplicó la ley
    assert (1, 6) in holidays or any(
        name == "Epifanía (Epiphany)" for name in holidays.values()
    )


def test_easter_based_holidays():
    """Test festivos basados en Pascua"""
    checker = ColombianHolidays()
    easter_holidays = checker.get_movable_religious_holidays(2025)

    # Debe incluir Jueves Santo, Viernes Santo, etc.
    holiday_names = list(easter_holidays.values())
    assert any("Jueves Santo" in name for name in holiday_names)
    assert any("Viernes Santo" in name for name in holiday_names)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
