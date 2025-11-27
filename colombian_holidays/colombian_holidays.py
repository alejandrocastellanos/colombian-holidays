"""
Colombian Holidays Library
===========================
A comprehensive library to check Colombian holidays following Law 51 of 1983 (Emiliani Law).
All Sundays are considered holidays in Colombia.
"""

from datetime import datetime, timedelta
from typing import Optional

from colombian_holidays.constants import FIXED_HOLIDAYS, MOVABLE_TO_MONDAY
from colombian_holidays.utils import calculate_easter, move_to_monday


class ColombianHolidays:
    """
    A class to handle Colombian holidays according to Law 51 of 1983 (Emiliani Law).
    """

    def __init__(self, date: Optional[datetime] = None):
        """
        Initialize the holidays checker.

        Args:
            date: The date to check. Defaults to today if not provided.
        """
        self.date = date or datetime.now()

    def get_movable_religious_holidays(self, year: int) -> dict:
        """
        Calculate Easter-based holidays that are moved to Monday.

        Args:
            year: The year for which to calculate holidays

        Returns:
            Dictionary with date tuples as keys and holiday names as values
        """
        easter = calculate_easter(year)

        # Calculate holidays based on Easter
        # Maundy Thursday (Easter - 3 days) - NOT moved
        maundy_thursday = easter - timedelta(days=3)

        # Good Friday (Easter - 2 days) - NOT moved
        good_friday = easter - timedelta(days=2)

        # Ascension (Easter + 43 days = Thursday, moved to following Monday = +46 days)
        ascension = easter + timedelta(days=43)
        ascension_monday = move_to_monday(ascension)

        # Corpus Christi (Easter + 64 days - already calculated to fall on Monday)
        corpus_christi = easter + timedelta(days=64)

        # Sacred Heart (Easter + 71 days - already calculated to fall on Monday)
        sacred_heart = easter + timedelta(days=71)

        return {
            (maundy_thursday.month, maundy_thursday.day): "Jueves Santo (Maundy Thursday)",
            (good_friday.month, good_friday.day): "Viernes Santo (Good Friday)",
            (ascension_monday.month, ascension_monday.day): "Ascensión del Señor (Ascension Day)",
            (corpus_christi.month, corpus_christi.day): "Corpus Christi",
            (sacred_heart.month, sacred_heart.day): "Sagrado Corazón (Sacred Heart)",
        }

    def get_all_holidays(self, year: int) -> dict:
        """
        Get all holidays for a given year.

        Args:
            year: The year for which to get holidays

        Returns:
            Dictionary with date tuples as keys and holiday names as values
        """
        holidays = {}

        # Add fixed holidays
        holidays.update(FIXED_HOLIDAYS)

        # Add movable holidays (moved to Monday by Emiliani Law)
        for (month, day), name in MOVABLE_TO_MONDAY.items():
            original_date = datetime(year, month, day)
            moved_date = move_to_monday(original_date)
            holidays[(moved_date.month, moved_date.day)] = name

        # Add Easter-based holidays
        holidays.update(self.get_movable_religious_holidays(year))

        return holidays

    def is_holiday(self, date: Optional[datetime] = None) -> bool:
        """
        Check if a given date is a holiday (including Sundays).

        Args:
            date: The date to check. Defaults to the instance's date if not provided.

        Returns:
            True if the date is a holiday, False otherwise
        """
        check_date = date or self.date

        # All Sundays are holidays
        if check_date.weekday() == 6:  # Sunday
            return True

        # Check official holidays
        holidays = self.get_all_holidays(check_date.year)
        return (check_date.month, check_date.day) in holidays

    def get_holiday_name(self, date: Optional[datetime] = None) -> Optional[str]:
        """
        Get the name of the holiday for a given date.

        Args:
            date: The date to check. Defaults to the instance's date if not provided.

        Returns:
            The name of the holiday, or None if not a holiday
        """
        check_date = date or self.date

        # Check if it's Sunday
        if check_date.weekday() == 6:
            return "Domingo (Sunday)"

        # Check official holidays
        holidays = self.get_all_holidays(check_date.year)
        return holidays.get((check_date.month, check_date.day))

    def is_today_holiday(self) -> bool:
        """
        Check if today is a holiday.

        Returns:
            True if today is a holiday, False otherwise
        """
        return self.is_holiday(datetime.now())

    def get_today_holiday_name(self) -> Optional[str]:
        """
        Get the name of today's holiday if it is one.

        Returns:
            The name of the holiday, or None if today is not a holiday
        """
        return self.get_holiday_name(datetime.now())


# Convenience functions
def is_today_holiday() -> bool:
    """
    Quick function to check if today is a holiday.

    Returns:
        True if today is a holiday, False otherwise
    """
    checker = ColombianHolidays()
    return checker.is_today_holiday()


def get_today_holiday_name() -> Optional[str]:
    """
    Quick function to get today's holiday name.

    Returns:
        The name of the holiday, or None if today is not a holiday
    """
    checker = ColombianHolidays()
    return checker.get_today_holiday_name()


def is_holiday(date: datetime) -> bool:
    """
    Quick function to check if a specific date is a holiday.

    Args:
        date: The date to check

    Returns:
        True if the date is a holiday, False otherwise
    """
    checker = ColombianHolidays(date)
    return checker.is_holiday()


def get_holiday_name(date: datetime) -> Optional[str]:
    """
    Quick function to get the holiday name for a specific date.

    Args:
        date: The date to check

    Returns:
        The name of the holiday, or None if not a holiday
    """
    checker = ColombianHolidays(date)
    return checker.get_holiday_name()


def list_holidays(year: int) -> dict:
    """
    List all holidays for a given year.

    Args:
        year: The year for which to list holidays

    Returns:
        Dictionary with date tuples as keys and holiday names as values
    """
    checker = ColombianHolidays()
    return checker.get_all_holidays(year)
