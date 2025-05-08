let idade = 17

if (idade<16) {
    var classeEleitoral = "Não-eleitor"
}
else if(idade>= 18 && idade<=65){
    classeEleitoral = "Eleitor obrigatório"
}
else if(idade>=16 && idade <18 || idade > 65){
    classeEleitoral = "Eleitor facultativo"
}
else{console.log("Valor inválido")}

console.log("Com " + idade+ " anos você é "+classeEleitoral)