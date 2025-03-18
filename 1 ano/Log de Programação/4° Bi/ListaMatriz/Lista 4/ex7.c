#include <stdio.h>

int main(){
	float matriz_A[10],matriz_B[10];
	int i;
	
	for (i=0;i<10;++i){
		printf("Digite um numero para a matriz A: ");
		scanf("%f", &matriz_A[i]);
	};
	printf("Os valores da Matriz B sao:\n");
	for (i=0;i<10;++i){
		matriz_B[i] = matriz_A[9-i];
		printf("%.2f\n", matriz_B[i]);
	};
	return 0;
}
