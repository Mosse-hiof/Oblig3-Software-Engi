# Oblig 2 gjort av Mustafa Sahin og Ibragim Yusupov

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    elif year % 4 != 0 or year % 400 != 0 and year % 100 == 0:
        return False
