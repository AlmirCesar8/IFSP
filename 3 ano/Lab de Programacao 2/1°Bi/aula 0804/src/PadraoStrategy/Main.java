package PadraoStrategy;
public class Main {
    public static void main(String[] args) {
        CalculadoraImposto calculadora = new CalculadoraImposto();
        double valor = 100.0;

        calculadora.setImposto(new Icms());
        System.out.println("Imposto ICMS: R$ " + calculadora.calcular(valor));

        calculadora.setImposto(new Iss());
        System.out.println("Imposto ISS: R$ " + calculadora.calcular(valor));
    }
}