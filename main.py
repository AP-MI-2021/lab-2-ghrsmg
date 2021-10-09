'''problema 10'''


def get_n_choose_k(n, k):
    nfact = 1
    kfact = 1
    mfact = 1
    m = n - k
    while (n):
        nfact = nfact * n
        n = n - 1
    while (k):
        kfact = kfact * k
        k = k - 1
    while (m):
        mfact = mfact * m
        m = m - 1
    print(nfact // (kfact * mfact))

def test_get_n_choose_k():
    '''Functia test '''
    assert get_n_choose_k(10, 8) == 45
    assert get_n_choose_k(12, 6) == 924
    assert get_n_choose_k(15, 10) == 3003

    '''problema 11'''


def get_leap_years(y1, y2):
    if y1 > y2:
        x = y1
        y1 = y2
        y2 = x
    for i in range(y1 - 1, y2 + 1, 1):
        if i % 4 == 0:
            print(i)


def test_get_leap_years():
    assert get_leap_years(2010, 2012) == 2012
    assert get_leap_years(2016, 2017) == 2016
    assert get_leap_years(2020, 2022) == 2020

    '''problema 12'''


def get_perfect_squares(start, end):
    for i in range(1, end + 1, 1):
        if i * i <= end and i * i >= start:
            print(i)


def test_get_perfect_squares():
    assert get_perfect_squares(2, 4) == 2
    assert get_perfect_squares(5, 9) == 3
    assert get_perfect_squares(10, 16) == 4


def main():
    n = int(input("Dati numarul: "))
    k = int(input("Dati numarul: "))
    while k != -1:
        print(get_n_choose_k(n, k))
        n = int(input("Dati alt numarul: "))
        k = int(input("Dati alt numarul: "))
    y1 = int(input("Dati anul: "))
    y2 = int(input("Dati numarul: "))
    while y2 != -1:
        print(get_leap_years(y1, y2))
        y1 = int(input("Dati alt an: "))
        y2 = int(input("Dati alt an: "))
    start = int(input("Dati numarul: "))
    end = int(input("Dati numarul: "))
    while end != -1:
        print(get_perfect_squares(start, end))
        start = int(input("Dati alt numar: "))
        end = int(input("Dati alt numar: "))
if __name__=='__main__':
    main()