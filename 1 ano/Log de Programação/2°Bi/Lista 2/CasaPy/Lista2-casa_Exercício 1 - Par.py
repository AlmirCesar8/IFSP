n = float(input("Digite sua nota para o arredondamento: "))
x = n % 1
if(x <= 0.5):
    na = n - x
else:
    na = int(n) + 1
print("Sua nota após o arredondamento foi: ", na)