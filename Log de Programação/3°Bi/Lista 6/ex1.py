unidade = input("Digite C para converter de Celsius para Fahrenheit\nDigite F para converter de Fahrenheit para Celsius\n")

def conversor(temp):
    cont = 0
    result = []
    if unidade == "C" or unidade == "c":
        while cont != len(temp):
            f = [temp[cont] * 9/5 + 32]
            result.append(f)
            cont +=1
    elif unidade == "F" or unidade == "f":
        while cont != len(temp):
            c = [(temp[cont] - 32)*5/9]
            result.append(c)
            cont +=1
    return result

l1 = [32, 64]
resultado = conversor(l1)
print(resultado)
