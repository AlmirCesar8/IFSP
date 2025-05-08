const a = 1, b = 2, c = 3

let menor, meio, maior

if (a <= b && a <= c) {
    menor = a
    if (b <= c) {
      meio = b
      maior = c
    } else {
      meio = c
      maior = b
    }
  } else if (b <= a && b <= c) {
    menor = b
    if (a <= c) {
      meio = a
      maior = c
    } else {
      meio = c
      maior = a
    }
  } else {
    menor = c
    if (a <= b) {
      meio = a
      maior = b
    } else {
      meio = b
      maior = a
    }
  }

console.log("Valores em ordem crescente:", menor, meio, maior)