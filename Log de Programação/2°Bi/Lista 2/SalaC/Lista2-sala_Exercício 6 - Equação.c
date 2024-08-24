#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c, d, x1, x2;

    printf("Insira A: ");
    scanf("%f", &a);
    printf("Insira B: ");
    scanf("%f", &b);
    printf("Insira C: ");
    scanf("%f", &c);

    if (a == 0){
        printf("Esta equacao nao eh do 2o grau");
    }
    else{
        d = pow(b,2) - (4 * a * c);
        if (d < 0){
            printf("Esta equacao sao nao tem raizes reais");
        }
        else{
            x1 = (-b + sqrt(d)) / (2 * a);
            x2 = (-b - sqrt(d)) / (2 * a);
            printf("As raizes dessa equacao sao: %.2f e %.2f", x1, x2);
        }
    }
}