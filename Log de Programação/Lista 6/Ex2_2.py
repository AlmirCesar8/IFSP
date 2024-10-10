c = str(input("Digite uma palavra: "))

def letramento(palavra):
    cont=0
    result = {}
    while cont != len(palavra):
        if palavra[cont] != " ":
            letra = palavra[cont]
            result[letra]= palavra.count(letra)
        cont+=1
    return result

resultado = letramento(c)
print(resultado)
