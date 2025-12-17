email = input("Digite seu email")
formatado = email.lower()
email2 = email.find("@")
dominio = email[email2:]
nome = input("Digite seu nome completo")
primeiro_nome = nome.find(" ")
primeiro_nome2 = nome[:primeiro_nome]
print(f"Seja bem vindo usuário {primeiro_nome2}!")
print(f"Seu cadastro foi registrado no email {formatado}, pertencente ao domínio {dominio}.")