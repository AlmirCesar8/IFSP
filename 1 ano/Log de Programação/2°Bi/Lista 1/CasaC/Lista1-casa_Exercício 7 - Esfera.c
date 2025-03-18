#include <stdio.h>
#include <math.h>

int main ()
{
    float r, V, A;

    printf("Digite o raio da esfera, em cm: ");
    scanf("%f", &r);
    V = ((4.0/3.0 * 3.14159) * (pow(r, 3)));
    A = (4 * 3.14159 * (pow(r, 2)));
    printf("A area da sua esfera eh de %.2f cm2 e seu volume eh de %.2f cm3", V, A);
}

