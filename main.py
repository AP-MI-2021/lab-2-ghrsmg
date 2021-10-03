'''problema 11'''
def get_leap_years(y1, y2):
    if y1 > y2:
        x = y1
        y1 = y2
        y2 = x
    for i in range(y1-1, y2+1, 1):
        if i % 4 == 0:
            print(i)


get_leap_years(2000, 2100)
