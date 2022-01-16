nota1 = input("Digite a primeira nota ")
nota2 = input("Digite a segunda nota ")
nota3 = input("Digite a terceira nota ")

media = (float(nota1)+float(nota2)+float(nota3))/3

print("Sua média é "+str(media))

if media >= 7:
    print("Você está aprovado! Parabéns, continue assim!")
elif media >= 5:
    print("Você está em recuperação, aproveite essa última chance!")
else:
    print("Você está reprovado, sinto muito, estude mais no próximo ano...")

