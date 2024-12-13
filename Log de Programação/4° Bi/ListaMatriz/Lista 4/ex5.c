#include <stdio.h>

int main(){
	float matriz_A[20],matriz_B[30],matriz_C[50];
	int i;
	
	for (i=0;i<20;++i){
		printf("Digite um numero para a matriz A: ");
		scanf("%f", &matriz_A[i]);
	};
	for (i=0;i<30;++i){
		printf("Digite um numero para a matriz B: ");
		scanf("%f", &matriz_B[i]);
	};
	printf("Os valores da Matriz C sao:\n");
	for (i=0;i<50;++i){
		if (i<20){
		   matriz_C[i] = matriz_A[i];
		}
		else{
			matriz_C[i] = matriz_B[i-20];
		}
		printf("%.2f\n", matriz_C[i]);
	};
	return 0;
}
