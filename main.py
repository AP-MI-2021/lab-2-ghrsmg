'''problema 10'''
'''def get_n_choose_k(n,k):
    nfact=1
    kfact=1
    mfact=1
    m=n-k
    while(n):
        nfact=nfact*n
        n=n-1
    while(k):
        kfact=kfact*k
        k=k-1
    while(m):
        mfact=mfact*m
        m=m-1
    print (nfact//(kfact*mfact))

def test_get_n_choose_k():
    if get_n_choose_k(10,8)==45 :
        pass
    if get_n_choose_k(12,6)==924:
        pass
    if get_n_choose_k(15,10)==3003:
        pass
''' '''problema 11''' '''
def get_leap_years(y1, y2):
    if y1 > y2:
        x = y1
        y1 = y2
        y2 = x
    for i in range(y1-1, y2+1, 1):
        if i % 4 == 0:
            print(i)


get_leap_years(2000, 2100)
'''
'''problema 12'''
def get_perfect_squares(start,end):
    for i in range(1,end+1,1):
        if i*i<=end and i*i>=start :
            print(i)
def test_get_perfect_squares ():
    if get_perfect_squares(2,4)== 2 :
        pass
    if get_perfect_squares(5,9)== 3:
        pass
