
const numero1 = 2;
const numero2 = 5;

function soma() {
    return numero1 + numero2;
}

const subtracao = (a, b) => a - b;

function multiplicacao() {
    return numero1 * numero2;
}

function divisao() {
    return (function (a, b) {
        if (b === 0) {
            throw new Error("Divisão por zero não é permitida.");
        }
        return a / b;
    })(numero1, numero2);
}

const raizQuadrada = () => {
    if (numero1 >= 0) {
        if (numero2 === 2) {
            return Math.sqrt(numero1);
        } else if (numero2 > 2) {
            return (numero1 ** (1 / numero2));
        } else {
            return null;
        }
    } else {
        if (numero2 % 2 === 0) {
            return null;
        } else {
            return -((-numero1) ** (1 / numero2));
        }
    }
}

const potenciacao = () => {
    return Math.pow(numero1, numero2);
}

console.log("Soma:", soma());
console.log("Subtração:", subtracao(numero1, numero2));
console.log("Multiplicação:", multiplicacao());
console.log("Divisão:", divisao());
console.log("Raiz Quadrada:", raizQuadrada());
console.log("Potenciação:", potenciacao());

