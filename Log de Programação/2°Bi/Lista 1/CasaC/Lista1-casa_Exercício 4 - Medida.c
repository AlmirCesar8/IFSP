#include<stdio.h>

int main()
{
	float a, b, A, P;
	
	printf("Digite a medida do lado a, em cm: ");
	scanf("%f", &a);
	printf("Digite a medida do lado b, em cm: ");
	scanf("%f", &b);
	A = (a * b);
	P = 2 * (a + b);
	printf("A area do retangulo eh igual a %.2f cm2, enquanto o perimetro eh igual a %.2f cm", A, P);
}
