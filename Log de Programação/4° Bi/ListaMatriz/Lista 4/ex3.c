#include <stdio.h>

int main(){
	float matriz_A[5],matriz_B[5],matriz_C[5];
	int i;
	
	for (i=0;i<5;++i){
		printf("Digite um numero para a matriz A: ");
		scanf("%f", &matriz_A[i]);
	};
	for (i=0;i<5;++i){
		printf("Digite um numero para a matriz B: ");
		scanf("%f", &matriz_B[i]);
	};
	printf("Os valores da Matriz C sao:\n");
	for (i=0;i<5;++i){
		matriz_C[i] = matriz_A[i] - matriz_B[i];
		printf("%.2f\n", matriz_C[i]);
	};
	return 0;
}
