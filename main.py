def get_perfect_squares(start,end):
    for i in range(1,end+1,1):
        if i*i<=end and i*i>=start :
            print(i)
def test_get_perfect_squares ():
    if get_perfect_squares(2,4)== 2 :
        pass
    if get_perfect_squares(5,9)== 3:
        pass
