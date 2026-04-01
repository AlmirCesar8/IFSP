public class Main {
    public static void main(String[] args) {
    // Testando a classe Mãe (Generalização)
    Pessoa p1 = new Pessoa("Carlos");
    p1.apresentar();
    // Saída: "Olá, sou Carlos"
    System.out.println("-------------------");
    // Testando a classe Filha (Especialização)
    Professor prof1 = new Professor("Carlos", "Informática");
    prof1.apresentar();
    // Saída: "Olá, sou o Prof. Carlos da área de Informática"
    }
}