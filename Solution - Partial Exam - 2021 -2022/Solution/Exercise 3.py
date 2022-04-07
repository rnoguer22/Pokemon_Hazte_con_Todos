#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def funcion_1(a, b, c):
    a = b - c
    b = c
    return b

def funcion_2(x, y, z):
    a = z
    b = x
    c = y
    
    a = b + c
    b = c
    return a
    

def funcion_3(m, n, l):
    a = m
    b = n
    c = l
    
    a = b - c
    b = c
    return a
    
def funcion_4(a, x, m):
#    a = z
    b = x
    c = m
    
    c = b + c
    b = c
    return b
        

def principal():
    a = 1
    b = 2
    c = 3
    m = 4
    n = 5
    l = 6
    x = 7
    y = 8
    z = 9
    
    funcion_2(a , b, c)
    
    print("Value of a : " + str(a))
    
    b = funcion_3(a , b, c)
    
    c = funcion_4(m , n, l)
    
    print("Value of c : " + str(c))
    
    funcion_1(x , y, z)


if __name__ == "__main__":
    principal()


# EOF