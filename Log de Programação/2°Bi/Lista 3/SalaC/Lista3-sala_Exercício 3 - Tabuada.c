#include <stdio.h>

int main()
{
	int tab, x;
	
	printf("Digite o numero da tabuada: ");
	scanf("%d", &x);
	for (tab = 1; tab < 11; tab++){
		printf("%d X %d = %d\n", x, tab, x * tab);
	}
}
