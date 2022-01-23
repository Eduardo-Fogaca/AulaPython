list_alunos = ["Joãozinho","Pedrinho"]
list_medias = [6,10]

if list_medias[0]>=7:
    print("Parabéns "+list_alunos[0]+", você está aprovado, com a média: "+str(list_medias[0]))
elif list_medias[0]>=5:
    print(list_alunos[0]+" você está de recuperação, com a média: "+str(list_medias[0]))
else:
    print(list_alunos[0]+" você foi reprovado, com a média: "+str(list_medias[0]))

if list_medias[1]>=7:
    print("Parabéns "+list_alunos[1]+", você está aprovado, com a média: "+str(list_medias[1]))
elif list_medias[1]>=5:
    print(list_alunos[1]+" você está de recuperação, com a média: "+str(list_medias[1]))
else:
    print(list_alunos[1]+" você foi reprovado, com a média: "+str(list_medias[1]))
