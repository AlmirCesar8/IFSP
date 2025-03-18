#include <stdio.h>

int main ()
{
    float p1, p2, atv, M;

    printf("Digite a nota da 1° prova: ");
    scanf("%f", &p1);
    printf("Digite a nota da 2° prova: ");
    scanf("%f", &p2);
    printf("Digite a nota das atividades: ");
    scanf("%f", &atv);
    M = ((p1 * 4 + p2 * 4 + atv * 2)/ 10);
    printf("Sua media no semestre foi %2.f", M);
}

