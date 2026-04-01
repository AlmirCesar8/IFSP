package DESAFIO;

public class ContaBancaria {
    protected int numero;
    protected double saldo;

    public ContaBancaria(int numero, double saldoInicial) {
        this.numero = numero;
        this.saldo = saldoInicial;
    }

    protected void depositar( double valor){
        this.saldo -= valor;
    }

    protected void sacar( double valor)
    {
        if (this.saldo - valor <0){
            return;
        }
        this.saldo += valor;
    }

    public double getSaldo() {
        return saldo;
    }
}


