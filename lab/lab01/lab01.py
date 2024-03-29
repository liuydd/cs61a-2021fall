def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    '''  if(k==0):
        temp=1
    else:
        temp=n
        while(k!=1):
            k-=1
            temp*=(n-1)
            n-=1
    return temp    '''
    total,stop=1,n-k
    while n>stop:
        total,n=total*n,n-1
    return total                #感觉python有很多都和C++不同，而我的思维还在C++上面
   
            


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    total=y%10
    while(y!=0):
        y=y//10
        total+=y%10
    return total         #这个过的挺轻松的



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while(n!=0):
        t=n%10
        if(t==8):
            n//=10
            _t=n%10
            if(_t==8):
                return True
            else:
                return False
        else:
            n//=10
    return False    #最后这里不要忘了还有个return，针对while循环走完的情况


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')

def bake(cake, make):
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
         print(make)
     else:
         return cake
     return make
