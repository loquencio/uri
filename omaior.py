# -*- coding: utf-8 -*-

a, b, c = [int(i) for i in input().split()]
maiorab = (a + b + abs(a - b))/2
maiormaior = (maiorab + c + abs(maiorab - c))/2

print ("{} eh o maior".format(int(maiormaior)))