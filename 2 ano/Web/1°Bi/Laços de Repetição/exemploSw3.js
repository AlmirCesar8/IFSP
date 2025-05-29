let mes = "Setembro"

switch (mes) {
    case "Dezembro":
    case "Janeiro":
    case "Fevereiro":
        console.log("Estação Verão")
        break;
    case "Março":
    case "Abril":
    case "Maio":
        console.log("Estação Outono")
        break;
    case "Junho":
    case "Julho":
    case "Agosto":
        console.log("Estação Inverno")
        break;
    case "Setembro":
    case "Outubro":
    case "Novembro":
        console.log("Estação Primavera")
        break;
    default:
        break;
}