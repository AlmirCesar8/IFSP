#include<stdio.h> 
int main()
{
	float V, T, D, LU;
	printf("Entre com a velocidade(km/h): ");
	scanf("%f", &V);
	printf("Entre com a tempo(h): ");	
	scanf("%f", &T);
	D = V * T;
	LU = D / 12;
	printf("A distancia percorrida foi de %.2f km, a velocidade media foi de %.2f km/h e tempo gasto foi de %.2f hora \n", V, T, D);
	printf("Foram usados %.2f litros", LU);
}
