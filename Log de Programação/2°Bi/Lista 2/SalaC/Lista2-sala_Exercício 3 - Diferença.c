#include <stdio.h>

int main()
{   
    float x, y, d;
    
    printf("Digite um numero: ");
    scanf("%f",&x);
    printf("Digite um segundo numero: ");
    scanf("%f",&y);
    if (x >= y){
        d = x - y;
        printf("Diferença entre %.2f e %.2f: %.2f", x, y, d);
    }
    else{
        d = y - x;
        printf("Diferença entre %.2f e %.2f eh %.2f", y, x, d);
    }
}