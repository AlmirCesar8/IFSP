import javax.swing.*;

public class exercicio  extends JFrame {
    public exercicio(){
        setTitle("primeira janela - LBP2");

        setSize(800, 600);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLocationRelativeTo(null);
    }

    public static void main(String[]args) {
        SwingUtilities.invokeLater(() -> {
            exercicio janela = new exercicio();

            janela.setVisible(true);
        });
    }
}

