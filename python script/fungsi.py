# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

# dokumentasi FIBONACCI

def fibo(n):
    if n > 2:
        res = fibo(n-1) + fibo(n-2)
    else:
        res = 1
    return res
#fibo(5)

#for i in range(10):
 #   print(fibo(i+1))
    
def recur(k):
    if(k > 0):
        res = k + recur(k - 1)
        print(res)
    else:
        res = 0
    return res

#print('\n\nrecursion example results')
#recur(6)

def faktor(n):

    faktor_i = math.factorial(n)
    return faktor_i
            
#print(faktor(n))