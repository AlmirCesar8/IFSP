c = str(input("Digite uma palavra: "))

def letramento(palavra):
    result = {}
    for letra in palavra:
        if letra != " ":   
            if letra in result:
                result[letra] += 1
            else:
                result[letra] = 1
    return result

resultado = letramento(c)
print(resultado)
 