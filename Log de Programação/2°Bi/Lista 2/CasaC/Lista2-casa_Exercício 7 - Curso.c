#include<stdio.h>

int main()
{
    int codigo;

    printf("Insira o codigo de acesso de seu curso: ");
    scanf("%i", &codigo);

    switch (codigo){
        case 1:
            printf("Engenharia");
            break;
        case 2:
            printf("Edificacoes");
            break;
        case 3:
            printf("Sistemas Eletricos");
            break;
        case 4:
            printf("Turismo");
            break;
        case 5:
            printf("Analise de Sistemas");
            break;
        default:
            printf("Codigo Invalido");
            break;

    }
}