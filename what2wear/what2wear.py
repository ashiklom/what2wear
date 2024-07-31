from datetime import date

from what2wear.holidays import is_holiday

def what2wear(dt: date) -> str:
    if is_holiday(dt):
        return "PJs"
    wday = dt.weekday()
    if wday in (1, 2, 3, 4):
        return "business"
    if wday == 5:
        # Casual Friday
        return "casual"
    elif wday in (0, 6) or is_holiday(dt):
        return "PJs"
    else:
        raise ValueError(f"Unknown weekday for date {dt}")
