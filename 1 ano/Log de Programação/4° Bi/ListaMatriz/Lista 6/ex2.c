#include <stdio.h>

void main() {
    float matriz_A[7], matriz_B[7], matriz_C[7][2];
    int i, j;

    for (i = 0; i < 7; ++i) {
            printf("Digite um numero para a matriz A: ");
            scanf("%f", &matriz_A[i]);
    };
    for (i = 0; i < 7; ++i) {
            printf("Digite um numero para a matriz B: ");
            scanf("%f", &matriz_B[i]);
    };
	for (i=0;i<7;++i){
		matriz_C[i][0] = matriz_A[i];
		matriz_C[i][1] = matriz_B[i];
	};
 printf("Os valores da matriz C são:\n");
    for (i = 0; i < 7; ++i) {
        printf("Linha %d: %.2f %.2f\n", i, matriz_C[i][0], matriz_C[i][1]);
    }
}
