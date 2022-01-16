dia = int(input("Digite o dia do seu nascimento "))
mes = int(input("Digite o seu mês de nascimento "))

if dia >= 22:
    if mes >= 8:
        print("Você é do tipo Fantasma/Planta")
    elif mes >= 4:
        print("Você é do tipo Fantasma/Água")
    else:
        print("Você é do tipo Fantasma/Fogo")
elif dia >= 11:
    if mes >= 8:
        print("Você é do tipo Elétrico/Planta")
    elif mes >= 4:
        print("Você é do tipo Elétrico/Água")
    else:
        print("Você é do tipo Elétrico/Fogo")
elif dia < 11:
    if mes >= 8:
        print("Você é do tipo Pedra/Planta")
    elif mes >= 4:
        print("Você é do tipo Pedra/Água")
    else:
        print("Você é do tipo Pedra/Fogo")
