nome = "Guilherme Luiz Souza Chinelati"
email = "timaomilgrau@hotmail.com"
posicao = email.find("@")
dominio = email[posicao:]
posicao_primeiro_nome = nome.find(" ")
primeiro_nome = nome[:posicao_primeiro_nome]
print(f"O usuário {primeiro_nome} foi cadastrado com sucesso no email {email} com domínio {dominio}")