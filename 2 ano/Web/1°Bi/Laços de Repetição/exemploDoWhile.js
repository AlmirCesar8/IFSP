do {
    var texto = "Feminino";
    var sexo = texto.charAt(0).toUpperCase()
    if (sexo != "F" && sexo != "M") {
        console.log("Erro, Validação de Sexo!")
        
    }
} while (sexo!="F" && sexo != "M");
console.log("Sexo validado")