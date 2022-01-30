list_alunos = ["Ana","Pedro","Vanessa","Eduardo"]
list_notas_alunos = [[8,7,6],[7,8,5],[10,4,6],[3,4,5]]
list_media = []
cont = 0
for list_nota in list_notas_alunos:
    media = (sum(list_nota))/3
    list_media.append(media)

for media in list_media:
    if media >=7:
        print("O aluno: "+list_alunos[cont]+" passou com média: "+str(media))
    elif media >=5:
        print("O aluno: "+list_alunos[cont]+" está em recuperação com média: "+str(media))
    else:
        print("O aluno: "+list_alunos[cont]+" reprovou com média: "+str(media))
    cont +=1
