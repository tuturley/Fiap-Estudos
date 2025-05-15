n = int(input("Digite um número: "))

lista_a = []
lista_b = []

for a in range(n + 1):
    for b in range(n + 1):
        if a + b == n:
            lista_a.append(a)
            lista_b.append(b)

print("Valores de a:", lista_a)
print("Valores de b:", lista_b)
