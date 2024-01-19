from leap_year import leap_year, is_leap_year

def test_old_leap_year():
    assert leap_year(2000) == ' 2000 is a Leap year'
    assert leap_year(2024) == ' 2024 is a Leap year'
    assert leap_year(2001) == ' 2001 is Not a Leap year'
    assert leap_year(2002) == ' 2002 is Not a Leap year'
    assert leap_year(2023) == ' 2023 is Not a Leap year'


def test_new_leap_year():
    assert is_leap_year(2024) == True
    assert is_leap_year(2028) == True
    assert is_leap_year(2032) == True
    assert is_leap_year(2036) == True
    assert is_leap_year(2040) == True
    assert is_leap_year(2044) == True
    assert is_leap_year(2048) == True
    assert is_leap_year(2052) == True
    assert is_leap_year(2056) == True

    assert is_leap_year(2023) == False
    assert is_leap_year(2025) == False
    assert is_leap_year(2027) == False
    assert is_leap_year(2029) == False
    assert is_leap_year(2031) == False
    assert is_leap_year(2033) == False
    assert is_leap_year(2035) == False
    assert is_leap_year(2037) == False
    assert is_leap_year(2039) == False