#include <stdio.h>

int main(){
    float matriz_A[5], matriz_B[5];
    int i;

    for (i=0; i<5;++i)
    {
        printf("Digite um numero para a matriz A: ");
        scanf("%f", &matriz_A[i]);
    };
    printf("Os valores da Matriz B sao:\n");
    for (i=0;i<5;++i){
        matriz_B[i] = matriz_A[i] * 3;
        printf("%.2f\n", matriz_B[i]);
    }
    return 0;
}
