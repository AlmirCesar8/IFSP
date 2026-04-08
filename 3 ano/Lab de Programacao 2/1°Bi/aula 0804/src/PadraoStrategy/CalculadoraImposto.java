package PadraoStrategy;
public class CalculadoraImposto {
    private ImpostoStrategy imposto;

    public void setImposto(ImpostoStrategy imposto) {
        this.imposto = imposto;
    }

    public double calcular (double valor){
        return imposto.calcular(valor);
    }
}
