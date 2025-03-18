#include <stdio.h>

int main ()
{
    float a, b ,c;

    printf("Digite um numero a: ");
    scanf("%f", &a);
    printf("Digite um numero b: ");
    scanf("%f", &b);
    c = a;
    a = b;
    b = c;
    printf("Apos a troca o a passa a ser: %.2f", a);
    printf("\nEnquanto o b passa a ser: %.2f", b);
}

