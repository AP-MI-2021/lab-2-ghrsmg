def get_n_choose_k(n,k):
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




