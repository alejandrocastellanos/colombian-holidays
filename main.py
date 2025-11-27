# Example usage
from datetime import datetime

from colombian_holidays import is_today_holiday, get_today_holiday_name, is_holiday, list_holidays, get_holiday_name

if __name__ == "__main__":
    # Check if today is a holiday
    if is_today_holiday():
        print(f"Today is a holiday: {get_today_holiday_name()}")
    else:
        print("Today is not a holiday")

    # Check a specific date
    specific_date = datetime(2025, 12, 25)
    if is_holiday(specific_date):
        print(f"{specific_date.strftime('%Y-%m-%d')} is: {get_holiday_name(specific_date)}")

    # List all holidays for 2025
    print("\nHolidays in 2025:")
    holidays_2025 = list_holidays(2025)
    sorted_holidays = sorted(holidays_2025.items(), key=lambda x: (x[0][0], x[0][1]))
    for (month, day), name in sorted_holidays:
        date_obj = datetime(2025, month, day)
        print(f"{date_obj.strftime('%Y-%m-%d (%A)')}: {name}")
