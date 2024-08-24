#include <stdio.h>

int main ()
{
    float n1, n2, n3, n4, M;

    printf("Digite a nota do 1° bimestre: ");
    scanf("%f", &n1);
    printf("Digite a nota do 2° bimestre: ");
    scanf("%f", &n2);
    printf("Digite a nota do 3° bimestre: ");
    scanf("%f", &n3);
    printf("Digite a nota do 4° bimestre: ");
    scanf("%f", &n4);
    M = (n1 + n2 + n3 + n4)/4;
    printf("Sua media final foi %2.f", M);
}

