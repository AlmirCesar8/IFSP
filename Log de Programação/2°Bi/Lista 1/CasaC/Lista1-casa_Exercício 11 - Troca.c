#include <stdio.h>

int main ()
{
    float a, b;

    printf("Digite um numero a: ");
    scanf("%f", &a);
    printf("Digite um numero b: ");
    scanf("%f", &b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("Apos a troca o a passa a ser: %.2f", a);
    printf("\nEnquanto o b passa a ser: %.2f", b);
}

