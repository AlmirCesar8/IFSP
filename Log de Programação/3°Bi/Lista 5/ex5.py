def primo(n):
    if n <= 1:
        return False
    for c in range(2, n):
        if n % c == 0:
            return False
    return True

n = int(input("Digite um número para a verificação: "))
print(primo(n))
