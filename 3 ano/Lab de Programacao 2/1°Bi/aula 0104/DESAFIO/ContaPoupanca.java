package DESAFIO;

public class ContaPoupanca extends ContaBancaria {
    public ContaPoupanca(int numero, double saldoInicial){
        super(numero, saldoInicial);
        
    }

    public void renderJuros(double taxa){
        this.saldo += this.saldo * taxa;

    }
    
}
