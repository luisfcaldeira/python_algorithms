
def leap_year(year: int) -> str:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f" {year} is a Leap year"
            else:
                return f" {year} is not a Leap year"
        else:
            return f" {year} is a Leap year"
    else:
        return f" {year} is Not a Leap year"
    

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    