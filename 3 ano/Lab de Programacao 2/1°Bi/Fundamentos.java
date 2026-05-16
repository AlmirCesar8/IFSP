public class Fundamentos {
    public static void main(String[] args) {
        // CONSTANTE: Valor fixo que não muda (Teoria: Segurança e Legibilidade)
        final double PI = 3.14159;
        
        // VARIÁVEIS: Espaços na RAM para dados mutáveis
        int idade = 20; // Inteiro (sem casas decimais)
        double saldo = 50.50; // Ponto Flutuante (com casas decimais)
        boolean temCartao = true;
        boolean temSaldo = saldo > 10;

        // OPERADORES LÓGICOS E CURTO-CIRCUITO (Aula 2)
        // No && (AND), se 'temCartao' for false, o Java nem olha o 'temSaldo'
        if (temCartao && temSaldo) {
            System.out.println("Compra autorizada!");
        } else if (!temCartao || saldo <= 0) { // Operador NOT (!) e OR (||)
            System.out.println("Verifique seus dados.");
        }
    }
}
// CLASSE: O molde para criar objetos
class Produto {
    // ATRIBUTOS: Definem o estado do objeto
    // private: Encapsulamento (só a classe acessa diretamente)
    private String nome;
    private double preco;

    // CONSTRUTOR: Chamado pelo 'new', tem o mesmo nome da classe
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    // MÉTODOS: Comportamentos do objeto
    public void exibirDetalhes() {
        System.out.println("Produto: " + nome + " | R$ " + preco);
    }
    
    // Getters/Setters: Forma segura de acessar atributos privados
    public double getPreco() { return preco; }
}
// HERANÇA (Relação "É UM"): Aluno é uma Pessoa
class Aluno extends Pessoa {
    private String prontuario;

    public Aluno(String nome, String prontuario) {
        // super(): Chama o construtor da Classe Mãe (Pessoa)
        super(nome); 
        this.prontuario = prontuario;
    }

    // SOBRESCRITA (@Override): Especialização do comportamento
    @Override
    public void apresentar() {
        // super.apresentar(): Reaproveita o comportamento da mãe e adiciona algo novo
        super.apresentar(); 
        System.out.println("Meu prontuário é: " + prontuario);
    }
}

// import java.nio.file.*;
// import java.io.*;

class GerenciadorArquivo {
    public static void main(String[] args) {
        Path caminho = Path.of("notas.txt");

        // TRY-WITH-RESOURCES: Fecha o arquivo automaticamente (Java 7+)
        // Evita vazamento de memória e erros de sistema operacional
        try (BufferedWriter escritor = Files.newBufferedWriter(caminho)) {
            escritor.write("Estudando POO - Java");
            System.out.println("Arquivo gravado com sucesso!");
        } catch (IOException e) {
            // Tratamento de exceção para erros de I/O (Input/Output)
            System.err.println("Erro ao manipular arquivo: " + e.getMessage());
        }
    }
}

// SINGLETON: Garante apenas uma instância no sistema todo
class LogManager {
    private static LogManager instancia;

    private LogManager() {} // Construtor privado: ninguém fora pode dar 'new'

    public static LogManager getInstancia() {
        if (instancia == null) {
            instancia = new LogManager();
        }
        return instancia;
    }
}

// FACTORY: Delega a criação para uma classe "Fábrica"
class InimigoFactory {
    public static Inimigo criarInimigo(String tipo) {
        if (tipo.equals("Orc")) return new Orc();
        if (tipo.equals("Troll")) return new Troll();
        return null;
    }
}

// INTERFACE: O contrato (Aula 6)
// Ela não tem código de execução, apenas diz que quem a "assinar"
// OBRIGATORIAMENTE precisará implementar o método calcular.
interface EstrategiaFrete {
    double calcular(double peso);
}

// IMPLEMENTAÇÃO 1: Frete Comum (Especialização)
class FreteComum implements EstrategiaFrete {
    @Override
    public double calcular(double peso) {
        // Regra específica da estratégia comum
        return peso * 1.5; 
    }
}

// IMPLEMENTAÇÃO 2: Frete Expresso (Especialização)
class FreteExpresso implements EstrategiaFrete {
    @Override
    public double calcular(double peso) {
        // Regra específica da estratégia expressa (mais cara)
        return peso * 3.5;
    }
}

// CONTEXTO: O sistema que usa a interface (Aula 6)
// O sistema não sabe QUAL frete está usando, ele apenas sabe que 
// o objeto possui o método .calcular() porque ele assinou o contrato.
class CalculadoraDeFrete {
    private EstrategiaFrete estrategia;

    // Injeção de dependência: permite trocar a estratégia dinamicamente
    public void setEstrategia(EstrategiaFrete estrategia) {
        this.estrategia = estrategia;
    }

    public void realizarCalculo(double peso) {
        double valor = estrategia.calcular(peso);
        System.out.println("O valor do frete selecionado é: R$ " + valor);
    }
}

// TESTE NO MAIN
public class ExemploInterface {
    public static void main(String[] args) {
        CalculadoraDeFrete calculadora = new CalculadoraDeFrete();

        // Usando a estratégia Comum
        calculadora.setEstrategia(new FreteComum());
        calculadora.realizarCalculo(10.0);

        // Trocando em tempo de execução para Expresso (Polimorfismo dinâmico)
        calculadora.setEstrategia(new FreteExpresso());
        calculadora.realizarCalculo(10.0);
    }
}