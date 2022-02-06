def calculadora(valor1,valor2,tipo_operacao):

    if tipo_operacao == "+":
        return valor1+valor2
    elif tipo_operacao == "-":
        return valor1-valor2
    elif tipo_operacao == "*":
        return valor1*valor2
    elif tipo_operacao == "/":
        return valor1/valor2
    else:
        print("Operação inválida")
        return

def insert_dados_calc():
    valor1 = float(input("Digite o valor 1: "))
    tipo_operacao = input("Digite a operação (+,-,*,/): ")
    valor2 = float(input("Digite o valor 2: "))

    print("Resultado: \n"+str(calculadora(valor1,valor2,tipo_operacao)))

insert_dados_calc()
