nome = input("Digite o seu nome ")
idade = input("Digite a sua idade ")
rua = input("Digite a sua rua ")
bairro = input("Digite o seu bairro ")
cep = input("Digite o seu CEP ")
cidade = input("Digite a sua cidade ")
opcao1 = input("Digite 1 para exibir os dados pessoais juntos ou 2 para exibir em linhas separadas: ")
opcao2 = input("Digite 1 para exibir os dados do endereço juntos ou 2 para exibir em linhas separadas: ")

if opcao1=="1":
    print("Seu nome é "+nome+" sua idade é "+idade+" anos")
else:
    print("Nome: "+nome+"\n"+"Idade: "+idade)

if opcao2=="1":
    print("Você mora na Rua: "+rua+" no Bairro "+bairro+" tem o CEP "+cep+" no Município de "+cidade)
else:
    print("Rua: "+rua+"\n"+"Bairro: "+bairro+"\n"+"CEP: "+cep+"\n"+"Cidade: "+cidade)
