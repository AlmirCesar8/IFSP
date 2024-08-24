#include <stdio.h>

int main()
{
    char nome[50];
    float salario;

    printf("Digite seu nome: ");
    fflush(stdin);
    fgets(nome, 50, stdin);
    printf("Digite seu salario: ");
    scanf("%f", &salario);

    if (salario <= 400){
        printf("\n%s%.2f\n15%%\n%.2f", nome, salario, salario + salario * 0.15);
    }
    else if (salario <= 700){
        printf("\n%s%.2f\n12%%\n%.2f", nome, salario, salario + salario * 0.12);
    }
    else if (salario <= 1000){
        printf("\n%s%.2f\n10%%\n%.2f", nome, salario, salario + salario * 0.10);
    }
    else if (salario <= 1800){
        printf("\n%s%.2f\n7%%\n%.2f", nome, salario, salario + salario * 0.07);
    }
    else if (salario <= 2500){
        printf("\n%s%.2f\n4%%\n%.2f", nome, salario, salario + salario * 0.04);
    }
    else if (salario > 2500){
    	printf("%s %.2f Sem aumento", nome, salario);
	}
	else{
		printf("Salario invalido");
	}
}
