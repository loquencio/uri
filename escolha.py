# -*- coding:utf-8 -*-

refeicoes = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
ind = 0
natend = 0

for i in refeicoes:
	natend += abs(i - p[ind]) if (i - p[ind]) < 0 else 0
	ind += 1  

print(natend)	