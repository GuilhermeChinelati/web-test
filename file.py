lista = ["banana", "maçã", "uva", "pera", "mamão"]
print(lista)
condicao = input("Deseja adicionar algum item à lista? ").lower().strip()
if condicao=="sim":
    item_add = input("Digite o item a ser adicionado ").lower()
    if item_add in lista:
        print("Este item já está na lista")
    else:
        lista.append(item_add)
        print(f"A lista atualizada é: {lista}")
else:
    print("Nenhum item será adicionado")
