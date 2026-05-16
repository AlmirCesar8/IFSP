import javax.swing.*;
import java.awt.*;

public class exercicio2 extends JFrame {
    public exercicio2(){
        setTitle("Login");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        setLayout(new BorderLayout());

        JPanel painelFormulario = new JPanel(new GridLayout(2,2));
        JLabel lblUtilizador = new JLabel("Utilizador:");
        JTextField txtUtilizador = new JTextField();
        JLabel lblSenha = new JLabel("Senha:");
        JPasswordField txtSenha = new JPasswordField();

        painelFormulario.add(lblUtilizador);
        painelFormulario.add(txtUtilizador);
        painelFormulario.add(lblSenha);
        painelFormulario.add(txtSenha);

        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton butao = new JButton("Entrar");
        butao.addActionListener(e -> {
            String texto = txtUtilizador.getText();
            String senha = new String(txtSenha.getPassword());

            if(texto.equals("admin") && senha.equals("1234")){
                JOptionPane.showMessageDialog(null, "Login efetuado com sucesso!");
            } else {JOptionPane.showMessageDialog(null, "Não foi possivel efetuar login");}
            txtUtilizador.setText("");
            txtSenha.setText("");
        });
        painelBotao.add(butao);

        add(painelFormulario, BorderLayout.CENTER);
        add(painelBotao, BorderLayout.SOUTH);


    }

    public static void main(String[] args){
        SwingUtilities.invokeLater(() -> {
            new exercicio2().setVisible(true);
        });
    }
}
