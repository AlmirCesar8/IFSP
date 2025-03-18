#include <stdio.h>
#include <math.h>

int main ()
{
    float t, s0, v0, a, S;

    printf("Digite o tempo da experiencia, em segundos: ");
    scanf("%f", &t);
    s0 = 2;
    v0 = 3;
    a = 10;
    S = (s0 + v0 * (1.0 / 2.0) * a * (pow(t,2)));
    printf("%.2f metros", S);
}

