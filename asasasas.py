m=int(input())
def season(m):
    if m==1 or m==2 or m==12:
        return 'winter'
    elif m == 3 or m == 4 or m==5:
        return 'spring'
    elif m == 6 or m==6 or m == 8:
        return 'summer'
    elif m == 9 or m == 10 or m == 11:
        return 'autumn'
    else:
        return 'ты конч....??????? такого месяца нет, отсталыш'
print(season(m))