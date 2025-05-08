const prova1 = 7
const prova2 = 8
const tr = 2
const faltas = 20

const media = ((prova1 * 0.4) + (prova2 * 0.6)) * 0.7 + tr

let situacao

if (media >= 6 && faltas < 24) {
  situacao = "Aprovado"
} else if (media >= 3 && media < 6 && faltas < 24) {
  situacao = "Exame"
} else if (faltas >= 24) {
  situacao = "Reprovado por faltas"
} else {
  situacao = "Reprovado"
}

console.log("Média do aluno:", media)
console.log("Situação do aluno:", situacao)