package dexv2;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URL;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import java.awt.BorderLayout;
import javax.swing.JInternalFrame;
import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JComboBox;

public class dex2 {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					dex2 window = new dex2();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public dex2() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBackground(Color.RED);
		frame.getContentPane().setBackground(Color.RED);
		frame.setBounds(100, 100, 900, 600);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JSplitPane SplitPrincipal = new JSplitPane();//division principal del primer frame
		
		JInternalFrame Datos = new JInternalFrame();//frame interno
		Datos.getContentPane().setBackground(Color.RED);
		
		JSplitPane SplitDatos = new JSplitPane();//division del frame interno
		SplitDatos.setSize(400,600);
		Datos.getContentPane().add(SplitDatos, BorderLayout.CENTER);
		
		pokelista comboBox = new pokelista();
		
		JLabel Imagendelpokimon = new JLabel();//label para las imagenes y su forma predefinida
		URL img = getClass().getResource("0.png");
		ImageIcon pkimg= new ImageIcon(img);
		Imagendelpokimon.setIcon(pkimg);
		SplitDatos.setLeftComponent(Imagendelpokimon);
		
		JTextArea textopokemon = new JTextArea("Información sobre el pokémon");//jtextarea para la informacion del pokemon
		//para hacer que el jtextarea se vea bien
		textopokemon.setLineWrap(true);
		textopokemon.setWrapStyleWord(true);
		SplitDatos.setRightComponent(textopokemon);
		
		
		SplitPrincipal.setRightComponent(Datos);
		Datos.setVisible(true);
		
		frame.getContentPane().add(SplitPrincipal, BorderLayout.CENTER);
		
		comboBox.Rellenalista();
		comboBox.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {//modifica imagen y texto al cambiar de pokemon en el jcombox
				Imagendelpokimon.setIcon(comboBox.mapa.get(comboBox.getSelectedItem()).getImagen());
				textopokemon.setText(comboBox.mapa.get(comboBox.getSelectedItem()).Informacion());
		//		System.out.println(comboBox.mapa.get(comboBox.getSelectedItem()).getImagen());
			}
		});
		
		SplitPrincipal.setLeftComponent(comboBox);

	}

}
