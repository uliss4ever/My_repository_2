import pytest
from Date.Date import Date, TimeDelta


@pytest.mark.parametrize("day,month,year,expected", [(1, 12, 2020, "01.12.2020")])
def test_create_date(day, month, year, expected):
    date = Date(day, month, year)
    assert str(date) == expected


@pytest.mark.parametrize("date, delta, expected", [
    ("20.07.2002", (1, 0, 0), "21.07.2002"),
    ("30.12.1453", (0, 1, 0), "30.01.1454")
])
def test_time_delta(date, delta, expected):
    d = Date(date)
    t = TimeDelta(delta[0], delta[1], delta[2])
    new_d = d + t
    assert new_d.__str__() == expected


@pytest.mark.parametrize("date1, date2, expected", [
    ("20.07.2002", "20.07.2002", 0),
    ("21.07.2002", "20.07.2002", 1)
])
def test_sub(date1, date2, expected):
    d1 = Date(date1)
    d2 = Date(date2)
    d3 = d2 - d1
    assert d3 == expected

# if __name__ == '__main__':
# test_sub(1, 12, 2021)
