list_vogal=["a","e","i","o","u"]

letra=str(input("Digite uma letra "))
txt = "É uma consoante"

for vogal in list_vogal:
    if letra==vogal:
        txt="É uma vogal"

print(txt)
