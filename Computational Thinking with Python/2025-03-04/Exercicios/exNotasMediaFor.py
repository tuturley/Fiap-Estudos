notas = []

n = int(input("Quantas notas você quer adicionar?: "))
j = 0+1
while j <= n:
    notas.append(j) 
    j += 1

print("A quantidade de notas é:", notas)
media = (len(notas) + len(notas))/n
print (media)


