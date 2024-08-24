#include <stdio.h>

int main ()
{
    float d, t, vm;

    printf("Digite a distancia percorrida, km: ");
    scanf("%f", &d);
    printf("Digite o tempo gasto, h: ");
    scanf("%f", &t);
    vm = d / t;
    printf("Sua velocidade media foi de %.2f km/h", vm);
}

