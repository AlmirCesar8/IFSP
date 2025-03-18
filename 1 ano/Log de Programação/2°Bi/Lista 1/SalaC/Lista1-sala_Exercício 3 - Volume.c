#include<stdio.h>
#include<math.h>

int main()
{
	float r, h, v;
	printf("Digite a medida do raio: ");
	scanf("%f", &r);
	printf("Digite a medida da altura: ");
	scanf("%f", &h);
	v = (3.14159 * (pow(r, 2)) * h);
	printf("O volume eh: %.2f", v);
}
