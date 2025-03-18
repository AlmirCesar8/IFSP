#include <stdio.h>

int main()
{
	float AP, LP, AA, LA, aP, aA, qntdA;
	
	printf("Digite a altura de sua parede, em metros: ");
	scanf("%f", &AP);
	printf("Digite a largura de sua parede, em metros: ");
	scanf("%f", &LP);
	printf("Digite a altura do azulejo, em metros: ");
	scanf("%f", &AA);
	printf("Digite a largura do azulejo, em metros: ");
	scanf("%f", &LA);
	aP = AP * LP;
	aA = AA * LA;
	qntdA = aP / aA;
	printf("Serao necessários %.2f azulejos para preencher a parede", qntdA);
}
