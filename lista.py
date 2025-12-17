lista_produtos = ["Mouse", "Procesadores Amd", "Monitores"]
print(lista_produtos)
remover = input("Digite o item a ser removido").title().strip()
lista_produtos.remove(remover)
print(f"A lista atualizada é: {lista_produtos}")