#include <stdio.h>

int main()
{
	float p, T, t, P;
	
	printf("Digite o valor da prestacao: ");
	scanf("%f", &p);
	printf("Digite o valor da taxa de juros: ");
	scanf("%f", &T);
	printf("Digite o tempo em atraso (em meses): ");
	scanf("%f", &t);
	P = (p + (p * (T / 100) * t));
	printf("O valor da prestacao atrasada e de: R$ %.2f", p);
}
