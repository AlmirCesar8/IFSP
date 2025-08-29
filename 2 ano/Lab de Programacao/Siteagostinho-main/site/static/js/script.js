class Pessoa {
    constructor(nome, ano_nascimento, endereco, curso, peso, altura) {
      this.nome = nome;
      this.ano_nascimento = ano_nascimento;
      this.endereco = endereco;
      this.curso = curso;
      this.peso = peso;
      this.altura = altura;
    }

    displayName() {
      return this.nome;
    }

    calcular_Idade(anoAtual) {
      return anoAtual - this.ano_nascimento;
    }

    imc() {
      return this.peso / (this.altura ** 2);
    }
  }

  const pessoa1 = new Pessoa("Carlos", 1995, "Rua das Flores, 123", "Engenharia", 70, 1.75);

  function mostrarNome() {
    const nome = pessoa1.displayName();
    document.getElementById("nomeDisplay").innerText = `Nome: ${nome}`;
  }

  function calcularIdade() {
    const ano = parseInt(document.getElementById("anoAtual").value);
    if (isNaN(ano)) {
      alert("Por favor, digite um ano válido.");
      return;
    }
    const idade = pessoa1.calcular_Idade(ano);
    document.getElementById("resultado").innerText = `Idade: ${idade} anos`;
  }

  function mostrarIMC() {
    const imc = pessoa1.imc().toFixed(2);
    document.getElementById("resultado").innerText = `IMC de ${pessoa1.nome}: ${imc}`;
  }





function filtrarNoticia() {
  fetch('/api/noticias')
    .then(response => response.json())
    .then(noticias => {
      const filtroSaude = document.getElementById('saude').checked;
      const filtroBemEstar = document.getElementById('bemEstar').checked;
      let categoriasSelecionadas = [];
      if (filtroSaude) categoriasSelecionadas.push('Saúde');
      if (filtroBemEstar) categoriasSelecionadas.push('Bem-Estar');
      // Se nenhum filtro selecionado, mostra todas
      let noticiasFiltradas = categoriasSelecionadas.length > 0
        ? noticias.filter(n => categoriasSelecionadas.includes(n.categoria))
        : noticias;
      let resposta = '';
      if (noticiasFiltradas.length === 0) {
        resposta = '<p>Nenhuma notícia encontrada para o filtro selecionado.</p>';
      } else {
        noticiasFiltradas.forEach(noticia => {
          resposta += `
            <article style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
              <h3>${noticia.titulo}</h3>
              <p>${noticia.resumo}</p>
              <p><strong>Categoria:</strong> ${noticia.categoria}</p>
            </article>
          `;
        });
      }
      document.getElementById('resultado').innerHTML = resposta;
    })
    .catch(err => {
      document.getElementById('resultado').innerHTML = '<p>Erro ao carregar notícias.</p>';
      console.error(err);
    });
}
// Chama a função ao carregar a página para mostrar todas as notícias inicialmente
window.onload = filtrarNoticia;