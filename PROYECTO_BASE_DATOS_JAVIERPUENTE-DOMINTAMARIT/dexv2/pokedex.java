package dexv2;

import java.util.*;

import java.io.*;

public class pokedex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean cerrar = false;
		List<List<String>> basedex = new ArrayList<List<String>>();
		System.out.println("Bienvenido a Pokémon Medac");
		String posicion = "ciudad";

		// introducir base de la pokedex
		try {//POR FAVOR INTRODUCE LA DIRECCION DE pokedex.txt  VIENE INCLUIDA CON EL PROGRAMA!!
			File base = new File("C:\\Users\\Domin\\workspace\\casa\\src\\dex\\pokedex.txt");
			Scanner sc = new Scanner(base);
			String datos = new String();
			String[] pokerray;

			while (sc.hasNextLine()) {
				datos = (sc.nextLine());
				pokerray = datos.split("/ ");

				List<String> poke2 = Arrays.asList(pokerray);
				// convertir string[] ---> arraylist<string>
				// basedex.add(spliteada);
				basedex.add(poke2);

				// System.out.println(poke2);/*testea la entrada desde fichero
				// */
			}
			// System.out.println(basedex.get(8).get(4)); /* así se ve cada
			// elemento*/

			sc.close();
		} catch (IOException e) {
			System.out.println("error de lectura: " + e);
		}

		HashMap<String, List<String>> pokedex = new HashMap<String, List<String>>();// hashmap para la pokedex
		HashMap<String, List<List<String>>> sitio = new HashMap<String, List<List<String>>>();// hashmap para la ruta																								

		// Declaracion de rutas

		List<List<String>> montaña = new ArrayList<List<String>>();// tipo fuego
																	// y roca
		for (int i = 1; i < basedex.size(); i++) {
			if (basedex.get(i).get(2).contains("fuego")) {
				montaña.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("roca")) {
				montaña.add(basedex.get(i));
			}
		}
		// for(int i =0;i<volcan.size();i++){
		// System.out.println(volcan.get(i));	//comprueba su contenido
		// }

		List<List<String>> isla = new ArrayList<List<String>>();// tipo agua y
																// hielo
		for (int i = 1; i < basedex.size(); i++) {
			if (basedex.get(i).get(2).contains("agua")) {
				isla.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("hielo")) {
				isla.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("dragon")) {
				isla.add(basedex.get(i));
			}
		}
		// for(int i =0;i<isla.size();i++){
		// System.out.println(isla.get(i));  //comprueba su contenido
		// }

		List<List<String>> ciudad = new ArrayList<List<String>>();// tipo
																	// psiquico
																	// lucha y
																	// hada
		for (int i = 1; i < basedex.size(); i++) {
			if (basedex.get(i).get(2).contains("psiquico")) {
				ciudad.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("hada")) {
				ciudad.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("lucha")) {
				ciudad.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("siniestro")) {
				ciudad.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("fantasma")) {
				ciudad.add(basedex.get(i));
			}
		}

		// for(int i =0;i<ciudad.size();i++){
		// System.out.println(ciudad.get(i));  //comprueba su contenido
		// }
		List<List<String>> selva = new ArrayList<List<String>>();// tipo veneno
																	// volador
																	// planta
																	// bicho
		for (int i = 1; i < basedex.size(); i++) {
			if (basedex.get(i).get(2).contains("veneno")) {
				selva.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("volador")) {
				selva.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("planta")) {
				selva.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("bicho")) {
				selva.add(basedex.get(i));
			}
		}
		// for(int i =0;i<bosque.size();i++){
		// System.out.println(bosque.get(i));
		// }

		List<List<String>> pradera = new ArrayList<List<String>>();// tipo
																	// normal
																	// tierra
																	// electrico
																	// acero
		for (int i = 1; i < basedex.size(); i++) {
			if (basedex.get(i).get(2).contains("normal")) {
				pradera.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("tierra")) {
				pradera.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("electrico")) {
				pradera.add(basedex.get(i));
			}
			if (basedex.get(i).get(2).contains("acero")) {
				pradera.add(basedex.get(i));
			}
		}
		// for(int i =0;i<pradera.size();i++){
		// System.out.println(pradera.get(i));
		// }

		sitio.put("montaña", montaña);
		sitio.put("isla", isla);
		sitio.put("selva", selva);
		sitio.put("ciudad", ciudad);
		sitio.put("pradera", pradera);

		for (int i = 1; i < basedex.size(); i++) {
			pokedex.put(basedex.get(i).get(0), basedex.get(i));
			pokedex.put(basedex.get(i).get(1), basedex.get(i));
		}

		/**/ do {
			int ale = (int) (Math.random() * sitio.get(posicion).size());
			// System.out.println(ale);

			////////////////////////

			Scanner sc = new Scanner(System.in);
			// eleccion de acciones
			System.out.println(
					"¿que desea hacer?\n¿Consultar pokedex,cambiar de ruta o capturar pokemon?\nElija: pokedex , ruta o capturar");
			String intro = sc.next();
			switch (intro) {/**/
			// parte de pokedex

			case "pokedex": { // revisado
				System.out.println("Ha elegido pokedex\n¿Quiere buscar por 'numero' o 'nombre'?");
				String elec = sc.next();
				if (elec.equals("numero")) {
					System.out.println("Introduce el numero del pokemon");
					String num = sc.next();
					int fail = Integer.parseInt(num);
					//System.out.println(fail);
					// System.out.println(num);
					if(fail>=basedex.size()){System.out.println("Fuera de rango\nPokedex nacional sin desbloquear");break;}
					

					System.out.println("¿Quieres ver su 'numero' , 'nombre' , 'tipo' , 'descripcion' o 'todo'");
					String busca = sc.next();
					switch (busca) {

					case "numero": {
						if (pokedex.get(num).get(6).equals("si")) {
							System.out.println(pokedex.get(num).get(0));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "nombre": {
						if (pokedex.get(num).get(6).equals("si")) {
							System.out.println(pokedex.get(num).get(1));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "tipo": {
						if (pokedex.get(num).get(6).equals("si")) {
							System.out.println(pokedex.get(num).get(2));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "descripcion": {
						if (pokedex.get(num).get(6).equals("si")) {
							System.out.println(pokedex.get(num).get(3));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "todo": {
						if (pokedex.get(num).get(6).equals("si")) {

							System.out.println("Numero: " + pokedex.get(num).get(0) + "\nNombre: "
									+ pokedex.get(num).get(1) + "\nTipo: " + pokedex.get(num).get(2));
							// }
							if (pokedex.get(num).get(5).equals("si")) {
								System.out.println("Descripcion: " + pokedex.get(num).get(3));
							}
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					default:
						System.out.println("respuesta mal introducida");
						break;
					}
				}

				// } // numero acaba aqui

				else if (elec.equals("nombre")) {
					System.out.println("introduce el nombre del pokemon");
					String nombre = sc.next();
					boolean fallo =true;
					List<String>paux=new ArrayList<String>();
					for(int i=0;i<basedex.size();i++){
						paux.add(basedex.get(i).get(1));
						
					if(	!paux.contains(nombre)){fallo =false;}
					}if(fallo){
						System.out.println("Ese pokemon no existe");
						break;}
					
					
					System.out.println("¿Quieres ver su 'numero' , 'nombre' , 'tipo' , 'descripcion' o 'todo'");
					String busca = sc.next();
					switch (busca) {

					case "numero": {
						if (pokedex.get(nombre).get(6).equals("si")) {
							System.out.println(pokedex.get(nombre).get(0));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "nombre": {
						if (pokedex.get(nombre).get(6).equals("si")) {
							System.out.println(pokedex.get(nombre).get(1));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "tipo": {
						if (pokedex.get(nombre).get(6).equals("si")) {
							System.out.println(pokedex.get(nombre).get(2));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "descripcion": {
						if (pokedex.get(nombre).get(6).equals("si")) {
							System.out.println(pokedex.get(nombre).get(3));
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					case "todo": {
						if (pokedex.get(nombre).get(6).equals("si")) {

							System.out.println("Numero: " + pokedex.get(nombre).get(0) + "\nNombre: "
									+ pokedex.get(nombre).get(1) + "\nTipo: " + pokedex.get(nombre).get(2));
							// }
							if (pokedex.get(nombre).get(5).equals("si")) {
								System.out.println("Descripcion: " + pokedex.get(nombre).get(3));
							}
						} else {
							System.out.println("no hay datos");
						}
						break;
					}

					default:
						System.out.println("respuesta mal introducida");
						break;
					}

				}

				else {
					System.out.println("Fallo al introducir elemento");
				}
				break;
			}

			// seleccion de ruta

			case "ruta": {
				System.out.println("\nEstas en la " + posicion);
				System.out.println("En esta zona aparecen los siguientes pokemon:\n");
				
				for(int i =0;i<sitio.get(posicion).size();i++){
				System.out.print(sitio.get(posicion).get(i).get(1)+"  ");
				if(i%4==0){
					System.out.println();}
				}
				
					System.out.println("\n¿Quieres hacer cambiar de ruta?\'si' o 'no'");	
				String respuesta = sc.next();
				if (respuesta.equals("si")) {
					System.out.println("¿A donde quieres ir?\n'ciudad', 'montaña', 'isla', 'pradera' o 'selva',");
					String cambio = sc.next();

					if (cambio.equals("montaña") || cambio.equals("isla") || cambio.equals("selva")
							|| cambio.equals("ciudad") || cambio.equals("pradera"))
						;
					{
						posicion = cambio;
					}
					System.out.println("Ahora estas en la " + posicion);
					System.out.println("En esta zona aparecen los siguientes pokemon:\n");
					
						for(int i =0;i<sitio.get(posicion).size();i++){
						System.out.print(sitio.get(posicion).get(i).get(1)+"  ");
						if(i%4==0){
							System.out.println();}
						}
						

				} else if(respuesta.equals("no")){System.out.println("Te quedas en "+posicion);break;}
				else {
					System.out.println("Introduce bien la ruta");
				}
				break;
			}

			case "capturar": {
				// pokemon random de la ruta//se guarda datos por avistamiento
				
				String aparece = sitio.get(posicion).get(ale).get(1);
				for (int i = 0; i < basedex.size(); i++) {
					if (basedex.get(i).get(1).equals(sitio.get(posicion).get(ale).get(1))) {
						basedex.get(i).set(6, "si");
					}
				}
				//
				// opciones del encuentro
				if(aparece.equals(basedex.get(151).get(1))){System.out.println("Encuentras un camión");}
				System.out.println("El pokemon aparecido es " + aparece + "\n ¿'capturar' o 'huir'?");
				String respuesta = sc.next();
				// huyes cual rattata
				if (respuesta.equals("huir")) {
					System.out.println("Sales corriendo");
					break;
				}

				else if (respuesta.equals("capturar")) {// seleccion de pokebal
														// y calculo de ratio de
														// captura
					System.out.println("¿Que pokeball vas a usar?\'pokeball' , 'superball' o 'ultraball' ");
					String ball = sc.next();
					int lanza = (int) (Math.random() * 100);
					int ratio = Integer.parseInt(sitio.get(posicion).get(ale).get(4));// convierte
																						// String
																						// a
																						// int
																						// ;p
					System.out.println("ratio de " + aparece + " es " + ratio);

					// eleccion de pokeball
					switch (ball) {
					/////

					case "pokeball": {// si se captura el valor atrapado se
										// actualiza a "si"
						System.out.println("ratio de captura de pokeball es " + lanza);
						if (lanza > ratio) {
							for (int i = 0; i < basedex.size(); i++) {
								if (basedex.get(i).get(1).equals(sitio.get(posicion).get(ale).get(1))) {
									basedex.get(i).set(5, "si");
								}
							}
							System.out.println(aparece + " Ha sido capturado, sus datos se guardaran en la pokedex");
						} else {
							System.out.println("El pokemon ha huido");
						}

						break;
					}

					/////
					case "superball": {//// si se captura el valor atrapado se
										//// actualiza a "si"
						lanza *= 1.5;// ratio de captura de la pokeball
						System.out.println("ratio de captura de superball es " + lanza);
						if (lanza > ratio) {
							for (int i = 0; i < basedex.size(); i++) {
								if (basedex.get(i).get(1).equals(sitio.get(posicion).get(ale).get(1))) {
									basedex.get(i).set(5, "si");
								}
							}
							System.out.println(aparece + " Ha sido capturado, sus datos se guardaran en la pokedex");
						} else {
							System.out.println("El pokemon ha huido");
						}

						break;
					}

					//////
					case "ultraball": {// si se captura el valor atrapado se
										// actualiza a "si"
						lanza *= 1.75;// ratio de captura de la pokeball
						System.out.println("ratio de captura de ultraball es " + lanza);
						if (lanza > ratio) {
							for (int i = 0; i < basedex.size(); i++) {
								if (basedex.get(i).get(1).equals(sitio.get(posicion).get(ale).get(1))) {
									basedex.get(i).set(5, "si");
								}
							}
							System.out.println(aparece + " ha sido capturado, sus datos se guardaran en la pokedex");
						} else {
							System.out.println("El pokemon ha huido");
						}
						break;
					}

					/////
					default:
						System.out.println("No has lanzado ninguna pokeball.\nEl pokemon se ha escapado");
					}
					break;
				}
			}

			default:
				System.out.println("introduzca los terminos indicados");
				break;
			}

			// terminador del ciclo
			System.out.println("\n¿Quieres salir del juego?");
			String acab = sc.next();
			if (acab.equals("si")) {
				cerrar = true;
			} else {
				System.out.println("Reiniciando...");
			}

		} while (!cerrar);
		// fin del juego
		System.out.println("Cerrando el juego...\nCerrado.");
	}
}
