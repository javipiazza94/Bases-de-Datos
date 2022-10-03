package dexv2;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.HashMap;

import javax.swing.JComboBox;


public class pokelista extends JComboBox{
	
	pokemon pokimon = new pokemon();
	HashMap<String,pokemon> mapa = new HashMap<String,pokemon>();
	public pokelista(){
		
	}
	
	public void Rellenalista(){//rellena el hashmap y el jcombox
		
		pokimon.LlenarDatos();
		for (int i=0;i<24;i++){//son 151
		this.addItem(pokimon.todosdatos.get(i).getNombre());
		mapa.put(pokimon.todosdatos.get(i).getNombre(),pokimon.todosdatos.get(i));
		
		//System.out.println(pokimon.todosdatos.get(i).getNombre());
		
		}
		
	}
	
}
