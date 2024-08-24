#include <stdio.h>

int main()
{   
    float n;
    
    printf("Digite um numero: ");
    scanf("%f",&n);
    
    if (n > 0){
        printf("O modulo desse numero eh: %.2f",n);
    }
    else{
        printf("O modulo desse numero eh: %.2f",n * (-1));
    }
}