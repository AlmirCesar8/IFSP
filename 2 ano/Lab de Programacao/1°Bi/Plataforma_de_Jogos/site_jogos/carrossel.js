const carrossel = document.getElementById('carrossel');
const itens = carrossel.querySelectorAll('.carrossel-item');
const prevBtn = document.querySelector('.carrossel-btn.prev');
const nextBtn = document.querySelector('.carrossel-btn.next');
let indice = 0;
const total = itens.length;

function atualizarCarrossel() {
    const largura = carrossel.offsetWidth;
    carrossel.style.transform = `translateX(${-indice * largura}px)`;
    carrossel.style.transition = 'transform 0.5s cubic-bezier(0.77, 0, 0.175, 1)';
}

// Botão próximo
nextBtn.addEventListener('click', () => {
    indice = (indice + 1) % total;
    atualizarCarrossel();
    reiniciarIntervalo();
});

// Botão anterior
prevBtn.addEventListener('click', () => {
    indice = (indice - 1 + total) % total;
    atualizarCarrossel();
    reiniciarIntervalo();
});

// Avanço automático infinito
let intervalo = setInterval(() => {
    indice = (indice + 1) % total;
    atualizarCarrossel();
}, 5000);

function reiniciarIntervalo() {
    clearInterval(intervalo);
    intervalo = setInterval(() => {
        indice = (indice + 1) % total;
        atualizarCarrossel();
    }, 5000);
}

// Responsivo: atualiza ao redimensionar a janela
window.addEventListener('resize', atualizarCarrossel);

// Inicializa o carrossel
atualizarCarrossel();