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

a = int(input("Digite o primeiro valor analisado"))
b = int(input("Digite o segundo valor analisado"))

resto_a = a % 2
resto_b = b % 2

if a > b:
    print("O valor {} é maior que {} " .format(a, b))
    if resto_a == 0:
        print("E representa um número par")
    else:
        print("E representa um número impar")
elif b > a:
    print("O valor {} é maior que {} ".format(b, a))
    if resto_b == 0:
        print("E representa um número par")
    else:
        print("E representa um número impar")
else:
    print("Os valores são iguais")
    if resto_a == 0:
        print("E representa um número par")
    else:
        print("E representa um número impar")
