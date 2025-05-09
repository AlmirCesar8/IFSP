class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    def detalhes(self):
        print(f"Livro: {self.titulo},\nAutor: {self.autor},\nNúmero de páginas: {self.numero_paginas}")

livros = [
    {
        'titulo': "Percy Jackson e o Ladrão de Raios",
        'autor': "Rick Riordan",
        'paginas': 400
    },
    {
        'titulo': "Harry Potter e a Pedra Filosofal",
        'autor': "JK Rolling",
        'paginas': 255
    },
    {
        'titulo': "Maze Runner: Correr ou Morrer",
        'autor': "James Dashner",
        'paginas': 408
    },
]

for livro in livros:
    livroObj = Livro(livro['titulo'], livro['autor'], livro['paginas'])
    livroObj.detalhes()




