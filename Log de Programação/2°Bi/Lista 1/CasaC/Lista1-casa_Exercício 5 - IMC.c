#include<stdio.h>
#include<math.h>

int main()
{
	float m, h, imc;
	
	printf("Digite seu peso(Kg): ");
	scanf("%f", &m);
	printf("Digite sua altura(m): ");
	scanf("%f", &h);
	imc = (m/(pow(h,2)));
	printf("Seu IMC eh igual a %.2f", imc);
}
