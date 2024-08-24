#include <stdio.h>

int main()
{
	float nrc, c;
	
	printf("Digite o numero de coelhos: ");
	scanf("%f", &nrc);
	c = ((nrc * 0.70) / 18 + 10);
	printf("O custo para manter esses coelhos sera de: R$ %.2f", c);
}
