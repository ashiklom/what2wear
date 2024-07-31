from datetime import date

from what2wear.holidays import is_holiday

def today() -> date:
    return date.today()

def what2wear(dt: date | None = None) -> str:
    if dt is None:
        dt = today()
    if is_holiday(dt):
        return "PJs"
    wday = dt.weekday()
    if wday in (0, 1, 2, 3):
        return "business"
    if wday == 4:
        # Casual Friday
        return "casual"
    elif wday in (5, 6) or is_holiday(dt):
        return "PJs"
    else:
        raise ValueError(f"Unknown weekday for date {dt}")

