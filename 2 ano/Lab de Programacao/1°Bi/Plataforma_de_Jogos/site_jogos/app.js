function jogar(){
    let div = document.getElementById("div-jogo");
    let resultado = '<div class="resultado"><img src="forca.png" alt="Imagem de uma forca"><input type="text" placeholder="Digite uma letra (A - Z)" id="input-letra"><button onclick="enviarLetra()" class="btn-enviar">Enviar</button></div>'

    div.innerHTML = resultado
}