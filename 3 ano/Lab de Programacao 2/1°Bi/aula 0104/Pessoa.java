// --- A CLASSE MÃE (Superclasse) ---
public class Pessoa {
    // PROTECTED: O nome está seguro contra acessos externos indesejados,
    // mas as classes filhas (como Professor e Aluno) têm permissão para usá-lo.
    protected String nome;
    public Pessoa(String nome) {
    this.nome = nome;
    }
    // Comportamento padrão da classe mãe
    public void apresentar() {
    System.out.println("Olá, sou " + this.nome);
    }
}