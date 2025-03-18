#include<stdio.h> 
int main()
{
	float r, d;
	printf("Digite, em reais, o valor: ");
	scanf("%f", &r);
    d = r / 2.40;
    printf("Esse valor eh igual a %.2f dolares", d);
}
