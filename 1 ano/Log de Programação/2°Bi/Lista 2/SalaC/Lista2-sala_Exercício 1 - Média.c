#include <stdio.h>

int main()
{   
    float n1,n2,n3,M;
    
    printf("Digite a 1 nota: ");
    scanf("%f",&n1);
    
    printf("Digite a 2 nota: ");
    scanf("%f",&n2);
    
    printf("Digite a 3 nota: ");
    scanf("%f",&n3);
    
    M = (n1 + n2 + n3) / 3;
    
    if (M >= 6){
        printf("Voce foi aprovado, sua media foi %.2f", M);
    }
    else{
        printf("Voce foi reprovado, sua media foi %.2f", M);
    }
}
