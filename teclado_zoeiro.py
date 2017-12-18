letras_n, frases_n = [int(i) for i in input().split()]
letras = {}
frases = {}

print(letras_n)

for i in range(letras_n):
	a, b = input().split()
	letras[a] = b

k, v = letras.items()

for i in range(frases_n):
	frases[] = input()


for frase in frases:
	for letra in frase: