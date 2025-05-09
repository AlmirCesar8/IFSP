let salario = 500
const salarioAntigo = salario
if(salario<500){
    salario += salario * 0.15
}
else if(salario>=500 && salario<=1000){
    salario += salario * 0.10
}
else{
    salario += salario * 0.05
}

console.log("O antigo salario era R$" + salarioAntigo + " e o novo é R$" + salario)