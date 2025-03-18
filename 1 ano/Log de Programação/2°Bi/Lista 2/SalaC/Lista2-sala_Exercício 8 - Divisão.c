#include <stdio.h>

int main()
{   
    int a, b, c;
    
    printf("Digite o numero A: ");
    scanf("%i",&a);
    printf("Digite o numero B: ");
    scanf("%i",&b);
    printf("Digite o numero C: ");
    scanf("%i",&c);
    if (a % 6 == 0){
        printf("%i eh divisivel por 2 e por 3\n", a);
    }
    if (b % 6 == 0){
        printf("%i eh divisivel por 2 e por 3\n", b);
    }
    if (c % 6 == 0){
        printf("%i eh divisivel por 2 e por 3\n", c);
    }
}