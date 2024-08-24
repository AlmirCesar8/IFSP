#include<stdio.h>

int main()
{
	float d, r;
	
	printf("Insira, em dolar, o valor: ");
	scanf("%f", &d);
	r = (d * 2.40);
	printf("Este valor e igual a %.2f reais", r);
}
