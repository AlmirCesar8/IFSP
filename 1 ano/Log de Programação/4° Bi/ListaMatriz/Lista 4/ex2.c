#include <stdio.h>
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
	
int main(){
	float matriz_A[6], matriz_B[6];
	int i;
	
	for	(i=0;i<6;++i){
		printf("Digite um numero para a matriz A: ");
		scanf("%f", &matriz_A[i]);	
	};
	printf("Os valores da Matriz B sao:\n");
	for (i=0; i<6; ++i){
		matriz_B[i] = fatorial(matriz_A[i]);
		printf("%.2f\n", matriz_B[i]);
	}
	return 0;
}
