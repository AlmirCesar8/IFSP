#include <stdio.h>

int main() 
{
    float valorA, valorB, valorC;

    printf("Digite o valor A: ");
    scanf("%f", &valorA);
    printf("Digite o valor B: ");
    scanf("%f", &valorB);
    printf("Digite o valor C: ");
    scanf("%f", &valorC);

    if (valorA > valorB && valorA > valorC && (valorB <= valorC)) {
        printf("%.2f, %.2f, %.2f\n", valorB, valorC, valorA);
    } 
    else if (valorA > valorB && valorA > valorC && (valorC <= valorB)) {
        printf("%.2f, %.2f, %.2f\n", valorC, valorB, valorA);
    } 
    else if (valorB > valorC && valorB > valorA && (valorC <= valorA)) {
        printf("%.2f, %.2f, %.2f\n", valorC, valorA, valorB);
    } 
    else if (valorB > valorC && valorB > valorA && (valorA <= valorC)) {
        printf("%.2f, %.2f, %.2f\n", valorA, valorC, valorB);
    } 
    else if (valorC > valorA && valorC > valorB && (valorB <= valorA)) {
        printf("%.2f, %.2f, %.2f\n", valorB, valorA, valorC);
    } 
    else if (valorC > valorA && valorC > valorB && (valorA <= valorB)) {
        printf("%.2f, %.2f, %.2f\n", valorA, valorB, valorC);
    }

}