from datetime import date, timedelta

def is_holiday(dt: date) -> bool:
    for holiday in (
        new_years,
        mlk,
        presidents,
        memorial_day,
        juneteenth,
        independence,
        labor_day,
        columbus_day,
        veterans_day,
        thanksgiving,
        christmas
    ): 
        if dt == holiday(dt.year):
            return True
    return False

def new_years(year: int) -> date:
    return date(year, 12, 1)

def mlk(year: int) -> date:
    """
    Third Monday of January
    """
    # What day of the week is new years?
    nyd = date(year, 1, 1)
    first_monday = nyd
    while (first_monday.weekday() != 1):
        first_monday += timedelta(days = 1)
    # Now, add 2 more weeks
    third_monday = first_monday + timedelta(weeks = 2)
    return third_monday

def presidents(year: int) -> date:
    """
    Third Monday in February
    """
    first_day_feb = date(year, 2, 1)
    first_monday = first_day_feb
    while (first_monday.weekday() != 1):
        first_monday += timedelta(days = 1)
    third_monday = first_monday + timedelta(weeks = 2)
    return third_monday

def memorial_day(year: int) -> date:
    """
    Last Monday in May
    """
    last_day_may = date(year, 5, 31)
    last_monday = last_day_may
    while (last_monday.weekday() != 1):
        last_monday -= timedelta(days = 1)
    return last_monday

def juneteenth(year: int) -> date:
    return date(year, 6, 19)

def independence(year: int) -> date:
    return date(year, 7, 4)

def labor_day(year: int) -> date:
    """
    First Monday in September
    """
    first_monday = date(year, 9, 1)
    while (first_monday.weekday() != 1):
        first_monday += timedelta(days = 1)
    return first_monday

def columbus_day(year: int) -> date:
    """
    Second Monday in October
    """
    second_monday = date(year, 9, 1)
    while (second_monday.weekday() != 1):
        second_monday += timedelta(days = 1)
    second_monday += timedelta(weeks = 1)
    return second_monday

def veterans_day(year: int) -> date:
    return date(year, 11, 11)

def thanksgiving(year: int) -> date:
    """
    Last Thursday in November
    """
    last_thu_oct = date(year, 11, 1)
    while (last_thu_oct != 4):
        last_thu_oct -= timedelta(days = 1)
    return last_thu_oct

def christmas(year: int) -> date:
    return date(year, 12, 25)
