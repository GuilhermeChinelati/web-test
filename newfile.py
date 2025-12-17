# exemplo 1
lista_produtos = ["mouse", "iphone", "placa de video"]
resposta = input("Deseja adicionar um item à lista?").strip()
if resposta == "sim":
    produto = input("Qual item você deseja adicionar?")
    lista_produtos.append(produto)
    print(lista_produtos)
else: 
    print("Então proseguiremos com o processo")
# exemplo 2
#Sem uso do elif
#salario = 7000
#vendas = float(input("faturamento das suas vendas"))
#if vendas>=15000:
   # salario += 5000
   # print(f"O novo salário é: {salario}")
#else:
   # if vendas>=8000:
      #  salario += 2500
      #  print(f"Seu novo salário será: {salario}")
#com uso do elif
salario = 6000
vendas = int(input("Digite suas vendas (apenas inteiros)"))
if vendas>=15000:
    salario += 1000
    print(f"O novo salário é: {salario}")
elif vendas>=4000:
    salario += 500
    print(f"Seu novo salário é: {salario}")
else:
    salario += 0
    print("Seu salário permanece 6000")