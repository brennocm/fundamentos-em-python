# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
#
# if a > b and a > 6:
#     print("O maior número é {}" .format(a))
# elif b > a and b > c:
#     print("O maior número é {}" .format(b))
# else:
#     print("O maior número é {}" .format(c))

valor = int(input("Digite o valor analisado"))
resto = valor % 2

if valor == 0:
    print("O valor é par")
else:
    print("O valor é impar")