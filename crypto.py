from sage.all import *
import requests
from Crypto.Util.number import long_to_bytes as l2b,bytes_to_long as b2l
from gmpy2 import gcd,is_prime,iroot

def factordb(n):
        s=[]
        url="http://factordb.com/api?query="+str(n)
        r = requests.get(url)
        factors=r.json()['factors']
        for f in factors:
                for i in range(f[1]):
                        s.append(int(f[0]))
        return s

def get_phin(n):
    pq = factordb(n)
    phin = 1
    for i in pq:
        phin *= i - 1
    return phin

def get_n(e, x):
    e,x = int(e),int(x)
    n = 10
    while pow(e, n) < x:
        n *= 10
    for i in range(len(str(n))-1):
        delta = (pow(10, len(str(n))-2 - i))
        while pow(e, n) > x:
            n -= delta
        if pow(e, n) == x:
            return n,True
        n += delta
    return n, False

