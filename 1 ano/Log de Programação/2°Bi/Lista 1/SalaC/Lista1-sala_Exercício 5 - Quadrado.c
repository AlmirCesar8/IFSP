#include<stdio.h>
#include<math.h>

int main()
{
	float n, q;
	
	printf("Digite um numero ");
	scanf("%f", &n);
	q = (pow(n, 2));
	printf("O quadrado desse numero e: %.2f", q);
}
