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

@pytest.mark.parametrize("date, expected", [(Date(23, 12, 1965), 23)])
def test_property_day(date, expected):
    assert date.day == expected
# что-то тут пока не то...
@pytest.mark.parametrize("day, value, expected", [(Date(23, 12, 1965), 23)])
def test_good_setter_year(date, expected):
    assert date.day == expected

@pytest.mark.parametrize("day, value, expected", [("32.2.1965", "Incorrect day")])
def test_bad_setter_day(date, expected):
    with pytest.raises(ValueError) as err:
        Date(date)
    assert err.value == expected

# @pytest.mark.parametrize
# @pytest.mark.parametrize

@pytest.mark.parametrize("date1, date2, expected", [
    ("20.07.2002", "20.07.2002", 0),
    ("21.07.2002", "20.07.2002", -1)
])
def test_sub(date1, date2, expected):
    d1 = Date(date1)
    d2 = Date(date2)
    d3 = d2 - d1
    assert d3 == expected

# if __name__ == '__main__':
# test_sub(1, 12, 2021)
