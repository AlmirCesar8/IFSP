#include<stdio.h>

int main()
{
	float F, C;
	printf("Entre com F: ");
	scanf("%f", &F);
	C = (((F - 32) * 5) / 9);
	printf("A temperatura em C e: %.2f", C);
}

