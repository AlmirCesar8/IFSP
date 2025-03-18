#include <stdio.h>>

int fatorial(int num){
	if (num == 0 || num == 1){
		return 1;
	}
	if (num < 0) {
        printf("Fatorial não definido para números negativos.\n");
        return -1;
	}
	return num * fatorial(num-1);
}

void main(){
	
	float matriz_A[10], matriz_B[10][3];
	int i,j;
	
	for (i=0;i<10;++i){
		printf("Digite um valor para a mariz A: ");
		scanf("%f", &matriz_A[i]); 
	}
	for (i=0;i<10;++i){
		matriz_B[i][0] = matriz_A[i] + 5;
		matriz_B[i][1] = fatorial(matriz_A[i]);
		matriz_B[i][2] = matriz_A[i] * matriz_A[i];
	}
	printf("Os valores da matriz B são:\n");
    for (i = 0; i < 10; ++i) {
        printf("Linha %d: %.2f %.2f %.2f\n", i, matriz_B[i][0], matriz_B[i][1], matriz_B[i][2]);
    }
}
