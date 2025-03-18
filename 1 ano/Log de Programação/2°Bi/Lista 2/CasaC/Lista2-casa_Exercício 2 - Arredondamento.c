#include<stdio.h>

int main()
{
    float n, r;

    printf("Digite sua nota para o arredondamento: ");
    scanf("%f", &n);
    r = n - (int)n;
    if (r <= 0.5){
        n = n - r;
    }
    else{
        n = (int)n + 1;
    }
    printf("Sua nota apos o arredondamento foi: %.2f", n);
}