#include <stdio.h>

int main() 
{
    float n1, n2, n3, maior, menor, meio;
    
    printf("Digite o primeiro numero: ");
    scanf("%f", &n1);
    printf("Digite o segundo numero: ");
    scanf("%f", &n2);
    printf("Digite o terceiro numero: ");
    scanf("%f", &n3);

    if (n1 >= n2 && n1 >= n3) {
        maior = n1;
    } else if (n2 >= n1 && n2 >= n3) {
        maior = n2;
    } else {
        maior = n3;
    }
    if (n1 <= n2 && n1 <= n3) {
        menor = n1;
    } else if (n2 <= n1 && n2 <= n3) {
        menor = n2;
    } else {
        menor = n3;
    }

    meio = (n1 + n2 + n3) - (maior + menor);
    printf("O maior numero eh: %.2f\n", maior);
    printf("O menor numero eh: %.2f\n", menor);
    printf("O numero do meio eh: %.2f\n", meio);
}
