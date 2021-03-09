import pytest
from class_Date import Date, TimeDelta


@pytest.mark.parametrize("date, delta, expected", [
    ("20.07.2002", (1, 0, 0), "21.07.2002"),
    ("30.12.1453", (0, 1, 0), "30.01.1454")
])
def test_time_delta(date, delta, expected):
    d = Date(date)
    t = TimeDelta(*delta)
    new_d = d + t
    assert str(new_d) == expected


@pytest.mark.parametrize("day,month,year,expected", [(1, 12, 2020, "01.12.2020")])
def test_create_date(day, month, year, expected):
    date = Date(day, month, year)
    assert str(date) == expected
    # assert repr(date) == expected


@pytest.mark.parametrize("day,month,year", [(29, 2, 2021)])
def test_create_date_bad(day, month, year):
    with pytest.raises(ValueError):
        Date(day, month, year)


@pytest.mark.parametrize("year, expected", [(2020, True), (2016, True), (2019, False)])
def test_is_leap_year(year, expected):
    assert Date.is_leap_year(year) == expected


@pytest.mark.parametrize("month, year, expected", [(2, 2028, 29), (1, 2020, 31), (2, 2021, 28)])
def test_get_max_day(month, year, expected):
    assert Date.get_max_day(month, year) == expected


@pytest.mark.parametrize("day, month, year, expected", [(31, 2, 2021, False)])
def test_is_valid_date(day, month, year, expected):
    assert Date.is_valid_date(day, month, year) == expected


@pytest.mark.parametrize("date, expected", [(Date(23, 12, 1965), 718059)])
def test_days_counter(date, expected):
    assert Date.days_counter(date) == expected


"""Сеттер и геттер дня"""


@pytest.mark.parametrize("date, day, expected", [(Date(31, 1, 1965), 31, "31")])
def test_property_day(date, day, expected):
    assert date.day == day


@pytest.mark.parametrize("date, day, expected", [(Date(28, 2, 2020), 29, "29.02.2020"),
                                                 (Date(7, 3, 1979), 9, "09.03.1979")
                                                 ])
def test_setter_day(date, day, expected):
    date.day = day
    assert str(date) == expected


@pytest.mark.parametrize("date, value, expected", [(Date(31, 1, 1965), 32, "Incorrect day")])
def test_setter_day_bad(date, value, expected):
    with pytest.raises(ValueError) as err:
        date.day = value
    assert str(err.value) == expected


"""Сеттер и геттер месяца"""

@pytest.mark.parametrize("date, month, expected", [(Date(23, 12, 1965), 12, "12")])
def test_property_month(date, month, expected):
    assert date.month == month


@pytest.mark.parametrize("date, month, expected", [(Date(29, 1, 2020), 2, "29.02.2020"),
                                                 (Date(7, 3, 1979), 9, "07.09.1979")
                                                 ])
def test_setter_month(date, month, expected):
    date.month = month
    assert str(date) == expected


@pytest.mark.parametrize("date, month, expected", [(Date(31, 1, 1965), 2, "Incorrect month")])
def test_setter_month_bad(date, month, expected):
    with pytest.raises(ValueError) as err:
        date.month = month
    assert str(err.value) == expected


"""Сеттер и геттер года"""


@pytest.mark.parametrize("date, year, expected", [(Date(23, 12, 1965), 1965, "1965")])
def test_property_year(date, year, expected):
    assert date.year == year


@pytest.mark.parametrize("date, year, expected", [(Date(29, 1, 2020), 1432, "29.01.1432"),
                                                 (Date(7, 3, 1979), 1976, "07.03.1976")
                                                 ])
def test_setter_year(date, year, expected):
    date.year = year
    assert str(date) == expected


@pytest.mark.parametrize("date, year, expected", [(Date(29, 2, 2020), 2021, "Incorrect year")])
def test_setter_year_bad(date, year, expected):
    with pytest.raises(ValueError) as err:
        date.year = year
    assert str(err.value) == expected

@pytest.mark.parametrize("date1, date2, expected", [
    ("20.07.2002", "20.07.2002", 0),
    ("21.07.2002", "20.07.2002", -1)
])
def test_sub(date1, date2, expected):
    d1 = Date(date1)
    d2 = Date(date2)
    d3 = d2 - d1
    assert d3 == expected


@pytest.mark.parametrize("date, timedelta, expected",
                         [(Date(2, 3, 1977), TimeDelta(3, 1, 1), Date(5, 4, 1978))])
def test_add(date, timedelta, expected):
    assert str(date + timedelta) == str(expected)



@pytest.mark.parametrize("date, timedelta, expected",
                         [(Date(2, 3, 1977), TimeDelta(3, 1, 1), Date(5, 4, 1978))])
def test_iadd(date, timedelta, expected):
    date += timedelta
    assert str(date) == str(expected)

# if __name__ == '__main__':
# test_sub(1, 12, 2021)
