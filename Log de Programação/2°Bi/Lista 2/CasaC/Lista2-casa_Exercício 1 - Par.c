#include <stdio.h>

int main()
{
    float n;
    printf("Digite um numero: ");
    scanf("%f", &n);
    if ((int)n % 2 == 0) {
        printf("%.2f eh um numero par", n);
    } else {
        printf("%.2f eh um numero impar", n);
    }

}