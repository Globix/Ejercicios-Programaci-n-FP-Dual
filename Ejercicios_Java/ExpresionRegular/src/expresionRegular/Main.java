package expresionRegular;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class Main {

	public static void main(String[] args) {
		
		//CASOS TEST PARA DNI'S INCORRECTOS
		//Siendo aleatorios los casos que utilizamos puede darse que algun caso puntual esté bien
		
		int numeroCasos = 10;
		String caso;
		ExpresionRegular expresionRegularDNI = new ExpresionRegular("\\b\\d{8}[A-Z&&[^IÃ‘OU]]\\b");
		
		ArrayList<String> casosTest = new ArrayList<>();
		
		for(int i = 1; i <= numeroCasos; i++){
			caso = "";
			for(int j = 1; j < 9; j++){
				Integer caracterAscii = ThreadLocalRandom.current().nextInt(48, 60); // 58 excluido
				caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			}
			Integer caracterAscii = ThreadLocalRandom.current().nextInt(65, 91);
			caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			casosTest.add(caso);
		}
		
		
		System.out.println("\n ***** Casos Test DNI FAIL ***** \n");
		
		for(String dni : casosTest){
			System.out.println(dni);
			
			expresionRegularDNI.comprobarSano(dni);
			
		}
		
		// //CASOS TEST PARA DNI'S CORRECTOS
		
		casosTest = new ArrayList<>();
		
		String[] casosTestPass = { //casos OK
				"78484464T","72376173A","01817200Q","95882054E","63587725Q",
				"26861694V","21616083Q","26868974Y","40135330P","89044648X",
				};
		
		System.out.println("\n ***** Casos Test DNI PASS ***** \n");
		
		for(String dni : casosTestPass){
			System.out.println(dni);
			
			expresionRegularDNI.comprobarSano(dni);
			
		}
		
		
		// CASOS TEST PARA NIE'S INCORRECTOS
		//Siendo aleatorios los casos que utilizamos puede darse que algun caso puntual esté bien
		
		numeroCasos = 10;
		expresionRegularDNI = new ExpresionRegular("\\b[XYZ]\\d{7}[A-Z&&[^IÑOU]]\\b");
		
		casosTest = new ArrayList<>();
		
		for(int i = 1; i <= numeroCasos; i++){
			caso = "";
			Integer caracterAscii = ThreadLocalRandom.current().nextInt(65, 88);
			caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			
			for(int j = 1; j < 9; j++){
				caracterAscii = ThreadLocalRandom.current().nextInt(48, 60); // 58 excluido
				caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			}
			caracterAscii = ThreadLocalRandom.current().nextInt(65, 91);
			caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			casosTest.add(caso);
		}
		
		
		System.out.println("\n ***** Casos Test NIE FAIL ***** \n");
		
		for(String dni : casosTest){
			System.out.println(dni);
			
			expresionRegularDNI.comprobarSano(dni);
			
		}
		
		// CASOS TEST PARA NIE'S CORRECTOS
		//Siendo aleatorios los casos que utilizamos puede darse que algun caso puntual no esté bien
		
		casosTest = new ArrayList<>();
		
		for(int i = 1; i <= numeroCasos; i++){
			caso = "";
			Integer caracterAscii = ThreadLocalRandom.current().nextInt(88, 91);
			caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			
			for(int j = 1; j < 8; j++){
				caracterAscii = ThreadLocalRandom.current().nextInt(48, 58);
				caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			}
			caracterAscii = ThreadLocalRandom.current().nextInt(65, 91);
			caso = caso + String.valueOf( Character.toChars(caracterAscii) );
			casosTest.add(caso);
		}
		
		
		System.out.println("\n ***** Casos Test NIE PASS ***** \n");
		
		for(String dni : casosTest){
			System.out.println(dni);
			
			expresionRegularDNI.comprobarSano(dni);
			
		}
			
		}

	}

