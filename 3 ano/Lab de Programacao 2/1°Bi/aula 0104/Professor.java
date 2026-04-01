public class Professor extends Pessoa {
    // Atributo específico do Professor.
    // Como ninguém herda de Professor (por enquanto), podemos usar private.
    private String area;
    public Professor(String nome, String area) {
    // O super() DEVE ser a primeira linha.
    // Mandamos o nome para a mãe inicializar a base do objeto.
    super(nome);
    this.area = area;
    }
    // A SOBRESCRITA: Mudando o comportamento padrão da mãe
    @Override
    public void apresentar() {
    // Note que conseguimos usar o 'this.nome' diretamente
    // porque ele foi declarado como 'protected' lá na classe Pessoa!
    System.out.println("Olá, sou o Prof. " + this.nome + " da área de " + this.area);
    }
}