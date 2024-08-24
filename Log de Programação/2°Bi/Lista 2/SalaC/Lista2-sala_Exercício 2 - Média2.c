#include<stdio.h>

int main()
{
	float n1, n2, M, e, nm;
	
	printf("Digite sua 1 nota: ");
	scanf("%f", &n1);
	printf("Digite sua 2 nota: ");
	scanf("%f", &n2);
	M = (n1 + n2)/2;
	if (M >= 6.0){
		printf("Voce foi aprovado, sua nota foi %.2f", M);
	}
	else {
		printf("Digite sua note no exame: ");
		scanf("%f", &e);
		nm = (M + e)/2;
		if (nm >= 5.0){
			printf("Voce foi aprovado em exame, sua nota foi %.2f", nm);
		}
		else{
			printf("Voce nao foi aprovado, sua nota apos o exame foi %.2f", nm);
		}
	}
}
