
function validar() {
    let p = document.getElementById("campo-resultado-validacao");
    let numero = parseInt(document.getElementById("campo-numero").value);
    // Inicializa uma string vazia para armazenar os resultados
    let resultado = "";

    if (numero>10) {
        resultado = "O número é maior que dez";
        p.style.color = "green";
    } else if (numero>5){
        resultado = "O número é maior que 5, mas menor ou igual a 10";
        p.style.color = "orange";
    } else {
        resultado = "O número é 5 ou menor";
        p.style.color = "blue";
    };

    if (!numero){
        resultado = "Por favor, insira um número.";
        p.style.color = "red";
    };

    p.innerHTML = resultado;
}