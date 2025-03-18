#include <stdio.h>

int main()
{   
    int A, B;
    
    printf("Digite um numero A: ");
    scanf("%i",&A);
    printf("Digite um numero B: ");
    scanf("%i",&B);
    if (A % 4 == 0){
        printf("%i eh divisivel por 4\n", A);
    }
    if (A % 5 == 0){
        printf("%i eh divisivel por 5\n", A);
    }
    if (B % 4 == 0){
        printf("%i eh divisivel por 4\n", B);
    }
    if (B % 5 == 0){
        printf("%i eh divisivel por 5\n", B);
    }
}