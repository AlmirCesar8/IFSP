// exemplo1 Switch case
//criando menu para estado civil

let opcao = 'A'.toLowerCase();

console.log("Escolha \n");
console.log("(S) - solteiro");
console.log("(C) - casado");
console.log("(D) - divorsiado\n");

switch (opcao) {
    case 's':
        console.log("Solteiro");
        break;

    case 'c':
        console.log("Casado");
        break;
    case 'd':
        console.log("Divorciado");
        break;
    default:
        console.log("Outros");
        break;
};