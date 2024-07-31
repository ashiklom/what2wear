from datetime import date
from unittest.mock import patch

import pytest

from what2wear.what2wear import what2wear 
from what2wear.holidays import is_holiday

dow_tests = (
    (date(2024, 7, 28), "PJs"),
    (date(2024, 7, 29), "business"),
    (date(2024, 7, 30), "business"),
    (date(2024, 7, 31), "business"),
    (date(2024, 8, 1), "business"),
    (date(2024, 8, 2), "casual"),
    (date(2024, 8, 3), "PJs")
)

@pytest.mark.parametrize("dt,expected", dow_tests)
def test_doy(dt, expected):
    assert what2wear(dt) == expected

# https://en.wikipedia.org/wiki/Thanksgiving_(United_States)#Date
thanksgivings = (
    date(2018, 11, 22),
    date(2019, 11, 28),
    date(2020, 11, 26),
    date(2021, 11, 25),
    date(2022, 11, 24),
    date(2023, 11, 23),
    date(2024, 11, 28)
)

@pytest.mark.parametrize("tg", thanksgivings)
def test_thanksgiving(tg):
    assert is_holiday(tg)

def test_today():
    with patch("what2wear.what2wear.today") as mock_date:
        mock_date.return_value = date(2024, 7, 27)
        assert what2wear() == "PJs"
        mock_date.return_value = date(2024, 7, 29)
        assert what2wear() == "business"

def test_fake_date():
    with pytest.raises(ValueError) as err:
        what2wear(date(2023, 2, 29))
    assert "day is out of range for month" in str(err)
