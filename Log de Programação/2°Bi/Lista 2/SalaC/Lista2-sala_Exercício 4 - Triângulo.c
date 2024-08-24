#include<stdio.h>

int main()
{
    float a, b, c;

    printf("Digite a medida dos lados: ");
    scanf("%f %f %f", &a, &b, &c);


    if ( (a < b + c) && (b < a + c) && (c < a + c)){
        if (a==b && c==b){
            printf("Triangulo Equilatero \n");
        }
        else{
            if (a!=b && c!=b){
                printf("Triangulo Escaleno \n");
            }
            else{
                printf("Triangulo Isoceles \n");
            }
        }
    }
    else{
        printf("Essas medidas nao sao validas para um triangulo \n");
    }
}
