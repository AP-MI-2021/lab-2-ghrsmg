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


get_n_choose_k(10, 6)

def test_get_n_choose_k():
    if get_n_choose_k(10, 8) == 45:
        pass
    if get_n_choose_k(12, 6) == 924:
        pass
    if get_n_choose_k(15, 10) == 3003:
        pass

'''problema 11'''

def get_leap_years(y1, y2):
    if y1 > y2:
        x = y1
        y1 = y2
        y2 = x
    for i in range(y1 - 1, y2 + 1, 1):
        if i % 4 == 0:
            print(i)


get_leap_years(2000, 2100)

'''problema 12'''


def get_perfect_squares(start, end):
    for i in range(1, end + 1, 1):
        if i * i <= end and i * i >= start:
            print(i)


def test_get_perfect_squares():
    if get_perfect_squares(2, 4) == 2:
        pass
    if get_perfect_squares(5, 9) == 3:
        pass

get_perfect_squares(70, 150)
def main() :
    n=int(input("Dati numarul: "))
    k = int(input("Dati numarul: "))
    while k!=-1:
        print(get_n_choose_k(n,k))
        n = int(input("Dati alt numarul: "))
        k = int(input("Dati alt numarul: "))
def main():
    y1 = int(input("Dati anul: "))
    y2= int(input("Dati numarul: "))
    while y2!=-1:
        print (get_leap_years(y1,y2))
        y1 = int(input("Dati alt an: "))
        y2 = int(input("Dati alt an: "))
def main():
    start = int(input("Dati numarul: "))
    end = int(input("Dati numarul: "))
    while end != -1:
        print(get_perfect_squares(start, end))
        start = int(input("Dati alt numarul: "))
        end = int(input("Dati alt numarul: "))



