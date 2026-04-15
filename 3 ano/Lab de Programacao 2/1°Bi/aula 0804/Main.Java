import java.util.Scanner;
interface PagamentoStrategy{
    double cobrar(double valor);
}

class Pix implements PagamentoStrategy{
    public double cobrar(double valor){
        return valor - (valor * 0.1);
    }
}

class CartaoCredito implements PagamentoStrategy{
    public double cobrar(double valor){
        return valor;
    }
}

class Criptomoeda implements PagamentoStrategy{
    public double cobrar(double valor){
        return valor - (valor * 0.2);
    }
}

class PagamentoFactory {
    public static PagamentoStrategy metodoPagamento(String metodo){
        if (metodo.equalsIgnoreCase("Pix")) {
            return new Pix();
        } else if (metodo.equalsIgnoreCase("Cartao de Credito")) {
            return new CartaoCredito();
        } else if (metodo.equalsIgnoreCase("Criptomoeda")){
            return new Criptomoeda();
        }
        throw new IllegalArgumentException("Método de pagamento inválido");
    }
}

class AuditoriaLog{
    private static AuditoriaLog instancia;
    private AuditoriaLog() { }
    
    public static synchronized AuditoriaLog getInstancia() {
        if (instancia == null) {
        instancia = new AuditoriaLog();
        }
        return instancia;
    }

    public void registrar(String msg) { 
        System.out.println("LOG: " + msg); 
    }
}

public class Main{
    public static void main (String[] args) {
        double valor_carrinho = 100.0;
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite como deseja pagar (Pix/Cartao de Credito/Criptomoeda): ");
        String metodo = scanner.nextLine();
        
        PagamentoStrategy metodoPagamento = PagamentoFactory.metodoPagamento(metodo);
        
        double valorFinal = metodoPagamento.cobrar(valor_carrinho);
        
        String log = "Pagamento de R$ " + valorFinal + " realizado via " + metodo;
        
        AuditoriaLog registro = AuditoriaLog.getInstancia();
        registro.registrar(log);
        
        scanner.close();
    }
}