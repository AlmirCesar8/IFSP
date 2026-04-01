package DESAFIO;

public class Main {

    public static void main(String[] args){
        ContaPoupanca conta1 = new ContaPoupanca(123, 5000.0);
        conta1.sacar(6000.0);
        conta1.renderJuros(4);
        System.out.println(conta1.getSaldo());

        ContaCorrente conta2 = new ContaCorrente(3000, 345, 1000);
        conta2.sacar(3500);
        System.out.println(conta2.getSaldo());
    }
}
