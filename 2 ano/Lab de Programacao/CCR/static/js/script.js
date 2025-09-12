document.addEventListener('DOMContentLoaded',()=> {
    const botoes = document.querySelectorAll('.seletor-personagem');
    const containerBiografia = document.getElementById('container-biografia');
    botoes.forEach(botao => {
        botao.addEventListener('click',() => {
            const personagemId = botao.dataset.id;
            containerBiografia.innerHTML = '<h2>Carregando...</h2><p></p>';

            // --- PONTO CRÍTICO ---

            fetch(`biografia/${personagemId}`)

            // 1. A primeira promessa do fetch retorna um objeto de Resposta HTTP.
            // Usamos response.json() para instruir o navegador a ler o corpo
            // da resposta e convertê-lo de uma string JSON para um objeto JavaScript
            // Este método retorna uma "nova promessa".

            .then(response => {
                if(!response.ok){
                    throw new Error('A resposta da rede não foi bem sucedida.');
                }
                return response.json();
            })

            // 2. O segundo .then() recebe o resultado da promessa anterior:
            // o objeto JavaScript ('data') já convertido.

            .then(data => {
                // Agora 'data' é um objeto com as chaves 'nome' e 'texto',
                // exatamente como no nosso dicionário Python.
                containerBiografia.innerHTML = `
                    <h2>${data.nome}</h2>
                    <p>${data.texto}</p>
                `;
            })
            .catch(error => {
                // Se qualquer passo acima falhar (rede, conversão do json, etc.),
                // este bloco será executado.
                console.error('Erro ao buscar a biografia:', error);
                containerBiografia.innerHTML = '<h2>Ocorreu um erro.</h2><p>Não foi possível carregar os dados. Verifique'
            })
        })
    })


    
})