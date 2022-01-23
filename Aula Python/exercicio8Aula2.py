list_alunos = []
list_medias = []

cont=0

while cont != 4:
    list_alunos.append(str(input("Digite o aluno: ")))
    list_medias.append(int(input("Digite a média do aluno: ")))
    cont +=1

cont=0

for media in list_medias:

    if int(media) >= 7:
        print("O Aluno: "+list_alunos[cont] + " Passou" + " com a média: "+ str(media))
    elif int(media) >=5:
        print("O Aluno: "+list_alunos[cont] + " Recuperação" + " com a media: "+ str(media))
    else:
        print("O Aluno: "+list_alunos[cont] + " Reprovou" + " com a média: "+ str(media))
    
    cont +=1
