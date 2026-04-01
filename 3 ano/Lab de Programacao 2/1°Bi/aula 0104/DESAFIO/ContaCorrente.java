package DESAFIO;

public class ContaCorrente extends ContaBancaria {
    private double limiteChequeEspecial;

    public ContaCorrente (double limiteChequeEspecial, int numero, double saldoInicial) {
        super(numero, saldoInicial);
        this.limiteChequeEspecial = limiteChequeEspecial;
        
    }
    @Override
    protected void sacar( double valor){
        if ((saldo + limiteChequeEspecial) - valor < 0){
            return;
        }
        saldo -= valor;
    }
    
}
