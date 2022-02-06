def dados_cadastrados():
    dict_dados = {
        1: "Josivaldo",
        2: "Juriscleudo",
        3: "Antonia",
        4: "Ronaldo"
    }

    return dict_dados

def verifica_dados(codigo):
    dict_cadastro= dados_cadastrados()
    list_codigo = dados_cadastrados().keys()

    if codigo in list_codigo:
        print(dict_cadastro[codigo])
    else:
        print("Código não cadastrado")

codigo = int(input("Digite um código: "))

verifica_dados(codigo)