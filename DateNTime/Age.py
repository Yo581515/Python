
from datetime import date


def age(dob):

    today = date.today()

    years = today.year - dob.year
    print(years)

    if (today.month , today.day) < (dob.month, dob.day):
        years -= 1

    return years


print('Age:', age(date(1997, 11, 8)))
