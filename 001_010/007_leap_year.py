def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


for year in [2000, 2024, 2035, 9090]:
    print("Is", year, "a leap year?", is_leap_year(year))


def count_leap_years():
    count = 0
    for year in range(0, 3001):
        if is_leap_year(year):
            count = count + 1
    return count


print("There are", count_leap_years(), "leap years from year 0 to 3000")
