dict_aluno = {}
list_notas = []

cont = 0
cont_nota = 0

while cont != 3:
    cont +=1
    aluno=input("Digite o nome do aluno: ")
    
    while cont_nota != 3:
        cont_nota +=1
        nota = float(input("Digite a nota "+str(cont_nota)+": "))
        list_notas.append(int(nota))

    cont_nota=0
    dict_aluno[aluno]=list_notas
    cont_nota=0
    list_notas=[]

list_alunos = dict_aluno.keys()

for aluno in list_alunos:
    media=(sum(dict_aluno[aluno]))/3
    if media >=7:
        print("O aluno: "+aluno+" está aprovado com a média: "+str(media))
    elif media >=5:
        print("O aluno: "+aluno+" está em recuperação com a média: "+str(media))
    else:
        print("O aluno: "+aluno+" está reprovado com a média: "+str(media))

