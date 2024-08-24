#include<stdio.h>

int main()
{
    float n;

    printf("Digite um numero: ");
    scanf("%f", &n);
    if (n>25){
        printf("A distancia de %.2f para 25 eh de: %.2f", n, (n - 25));
    }
    else{
        printf("A distancia de %.2f para 25 eh de: %.2f", n, (25 - n));
    }
}