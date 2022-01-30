dict_algarismosRomanos = {"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX","10":"X"}

numero = input("Digite um número de 1 a 10: ")

for romano in numero:
    print(dict_algarismosRomanos[romano])


