#include<stdio.h>
#include <string.h>

int main()
{
    char x[2];
    int c = 0, p = 0, i = 0;
    int f1 = 0, f2 = 0, f3 = 0, f4 = 0, f5 = 0;
    float n, maior, menor, m;
    m = 0;

    while (1)
    {
        printf("Digite um numero: ");
        scanf("%f", &n);
        printf("Deseja continuar (S/N)? ");
        scanf("%s", x);

        m += n;
        ++c;

        if (c == 1){
            maior = menor = n;
        }

        if (n > maior){
            maior = n;
        }
        if (n < menor){
            menor = n;
        }

        if ((int)n % 2 == 0){
            ++p;
        }
        else{
            ++i;
        }
        
        if (n<0){
            ++f1;}

        else if (0 <= n && n < 15){
            ++f2;
        }
        else if (15 <= n && n < 100){
            ++f3;
        }
        else if (100 <= n && n < 1000){
            ++f4;
        }
        else{
            ++f5;
        }

       if (strcmp(x, "N") == 0 || strcmp(x, "n") == 0){
        printf("Encerrando...\nObrigado por usar\n");
        break;
       }
    }
    printf("\nA media aritimetrica entre esses numeros eh: %.2f\n", m/c);
    printf("O maior numero entre esses eh: %.2f\n", maior);
    printf("O menor numero entre esses eh: %.2f\n", menor);
    printf("O total de numeros pares foi: %d\n", p);
    printf("O total de numeros impares foi: %d\n", i);
    printf("O total de elementos na faixa 1 foi: %d\n", f1);
    printf("O total de elementos na faixa 2 foi: %d\n", f2);
    printf("O total de elementos na faixa 3 foi: %d\n", f3);
    printf("O total de elementos na faixa 4 foi: %d\n", f4);
    printf("O total de elementos na faixa 5 foi: %d\n", f5);
}