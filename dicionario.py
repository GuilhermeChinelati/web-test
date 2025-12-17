dicionario = {"notebook":3000, "monitor":5000, "processador":6000}
print(dicionario)
processo = input("Deseja remover algum item da base? (sim/não)").lower().strip()
if processo=="sim":
    item_removido = input("Digite o item a ser removido").lower().strip()
    dicionario.pop(item_removido)
    print(f"A lista sem o item {item_removido} é {dicionario}")
else:
    print("Então proseguiremos")

adicionar = input("Deseja adicionar algum item na base? (sim/não)").lower().strip()
if adicionar=="sim":
    item_add = input("Digite o item a ser adicionado").lower().strip()
    preco_item = int(input("Digite o preço do item adicionado (apenas números)"))
    if item_add in dicionario:
        print("Este item já está em nossa base")
    else:
        dicionario[item_add] = preco_item
        print(f"A lista atualizada é: {dicionario}")
else:
    print("Nenhum item será adicionado")

    