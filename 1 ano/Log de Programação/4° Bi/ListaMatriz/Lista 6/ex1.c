#include <stdio.h>

void main() {
    float matriz_A[5][3], matriz_B[5][3], matriz_C[5][3];
    int i, j;

    for (i = 0; i < 5; ++i) {
        for (j = 0; j < 3; ++j) {
            printf("Digite um numero para a matriz A: ");
            scanf("%f", &matriz_A[i][j]);
        };
    };
    
	for (i = 0; i < 5; ++i) {
        for (j = 0; j < 3; ++j) {
            printf("Digite um numero para a matriz B: ");
            scanf("%f", &matriz_B[i][j]);
        };
	};
	    
	for (i = 0; i < 5; ++i) {
        for (j = 0; j < 3; ++j) {
            matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j];
            printf("%.2f\n",matriz_C[i][j]);
        };
    };
}
