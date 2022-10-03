package dexv2;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import javax.swing.ImageIcon;
import javax.swing.JButton;

public class pokemon {
	private int numero;
	private String nombre;
	private String tipo;
	private String desc;
	private ImageIcon imagen;
	ArrayList<pokemon> todosdatos = new ArrayList<pokemon>();
	
	
	public pokemon(){
		
		
	}

	
	
	/**
	 * @return the todosdatos
	 */
	public ArrayList<pokemon> getTodosdatos() {
		return todosdatos;
	}



	/**
	 * @param todosdatos the todosdatos to set
	 */
	public void setTodosdatos(ArrayList<pokemon> todosdatos) {
		this.todosdatos = todosdatos;
	}



	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getDesc() {
		return desc;
	}

	public void setDesc(String desc) {
		this.desc = desc;
	}

	public ImageIcon getImagen() {
		return imagen;
	}

	public void setImagen(ImageIcon imagen) {
		this.imagen = imagen;
	}
	
	public void LlenarDatos(){//metodo para extraer informacion del txt, crear lo pokemon y meterlos en el array
		
		for(int i =0;i<3;i++){
		
		try {
			File base = new File("C:\\Users\\DAM\\workspace\\nuevo\\src\\dexv2\\pokedex.txt");
			Scanner sc = new Scanner(base);
			String datos = new String();
			String[] pokerray;

			for (int j =0;j<24;j++)//rellena los datos de lpokemon
//			while (sc.hasNextLine()) este es el que debe entrar
			{
				datos = (sc.nextLine());
				pokerray = datos.split("/ ");
				todosdatos.add(new pokemon());
//				System.out.println(pokerray[0]);
//				System.out.println(pokerray[1]);
//				System.out.println(pokerray[2]);
//				System.out.println(pokerray[3]);
				todosdatos.get(j).setNumero(Integer.parseInt(pokerray[0]));
				todosdatos.get(j).setNombre(pokerray[1]);
				todosdatos.get(j).setTipo(pokerray[2]);
				todosdatos.get(j).setDesc(pokerray[3]);
				
				URL img = getClass().getResource((j)+".png");
				ImageIcon pkimg= new ImageIcon(img); 
				todosdatos.get(j).setImagen(pkimg);
//				System.out.println(todosdatos.get(j).nombre);
				
			}
			
			sc.close();
			} 
		catch (IOException e) {System.out.println("error de lectura: " + e);}
		
		}
	}



	private void setIcon(ImageIcon pkimg) {
		// TODO Auto-generated method stub
		
	}
	
	public String Informacion(){//da la informacion del pokemon
		String res = this.numero + "."+this.nombre + "\n\n"+this.tipo+"\n"+this.desc;
		
	//	System.out.println(res);//comprueba si funciona
		return res;
	}
}
		
	
	



