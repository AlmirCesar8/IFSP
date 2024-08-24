#include<stdio.h>

int main()
{
	float a, b, c, d;
	printf("Digite um valor a: ");
	scanf("%f", &a);
	printf("Digite um valor b: ");
	scanf("%f", &b);
	c = ((a * b) / a);
	d = ((a * b) / b);
	a = c;
	b = d;
	printf("Apos a troca o valor de a passa a ser %.2f\n", a);
	printf("enquanto o valor de b passa a ser %.2f", b);
}
