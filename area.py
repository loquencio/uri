# -*- coding: utf-8 -*-

a, b, c = [float(i) for i in input().split()]

print("TRIANGULO: {:0.3f}".format((a * c)/2))
print("CIRCULO: {:0.3f}".format((3.14159 * (c * c))))
print("TRAPEZIO: {:0.3f}".format(((a + b) * c)/2))
print("QUADRADO: {:0.3f}".format(b*b))
print("RETANGULO: {:0.3f}".format(a*b))