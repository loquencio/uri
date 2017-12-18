# -*- coding: utf-8 -*-

import re

rodizio = {'MONDAY' : [1, 2], 'TUESDAY' : [3, 4], 'WEDNESDAY' : [5, 6], 'THURSDAY' : [7, 8], 'FRIDAY' : [0, 9]}
padrao = re.compile("(^[A-Z]{3}-[0-9]{4}$)")
n = int(input())
placas = []

for i in range(n):
	placas.append(input())


for i in placas:
	if ( not padrao.match(i)):
		print("FAILURE")
	else:
		valor = int(i[-1])
		for k, v in rodizio.items():
			if (valor in v):
				print(k)
				break
			