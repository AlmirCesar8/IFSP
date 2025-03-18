#include <stdio.h>
#include <math.h>

int main() 
{
    float r, A, C;
    
    printf("Digite o raio da circunferencia, em cm: ");
    scanf("%f", &r);
    A = (3.14159 * (pow(r,2)));
    C = (2 * 3.14159 * r);
    printf("A area da sua circunferencia eh %.2f cm2 e seu comprimento eh de %.2f cm", A, C);
}

