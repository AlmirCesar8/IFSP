#Carrinho de Compras
op = input("Você deseja adicionar algo no carrinho?(S/N): ").upper()
carrinho = [
]
valor_carrinho = 0

while op == "S":
    if op == "N":
        break
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    carrinho.append(produto)
    print("Produto adicionado com sucesso!")
    op = input("Você deseja adicionar mais algo no carrinho?(S/N): ")
    while op != "N" and op != "S":
        print("Opção inválida! Tente novamente.")
        op = input("Você deseja adicionar mais algo no carrinho?(S/N): ").upper()

print("\n--- Carrinho de Compras ---")
if not carrinho:
    print("Carrinho vazio")
else:     
    for produto in carrinho:
        print(f"\nProduto: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
        valor_total = produto['preco'] * produto['quantidade']
        print(f"Valor total do produto: {valor_total}")
        valor_carrinho += valor_total
    print(f"\nValor final do carrinho é: {valor_carrinho}")

