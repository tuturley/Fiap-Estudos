fila = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4']
print("Fila atual:", fila)

funcao = input("Você quer adicionar ou remover uma pessoa? (add ou rem): ")

if funcao == 'add':
    adicionar = input("Qual nome você quer adicionar?: ")
    fila.append(adicionar) 
    print("Fila atualizada:", fila)

elif funcao == 'rem':
    if len(fila) > 0:
        removido = fila.pop(0) 
        print(f"{removido} foi removido da fila.")
    else:
        print("A fila está vazia, não há ninguém para remover.")
    print("Fila atualizada:", fila)

else:
    print("Não tem essa opção. Digite 'add' para adicionar ou 'rem' para remover.")
