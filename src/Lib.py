import math
import os

global primes
primes = []

def removeImg(path):
    os.remove(path)

def to2d(image):
    data = []
    pix = image.load()
    for x in xrange(image.size[0]):
        data.append([pix[x,y] for y in xrange(image.size[1])])
    return data

def distanceFromPoint(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def isprime(x):
    return primes.index(x) != None

def genPrimes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

primes = genPrimes(2000000)