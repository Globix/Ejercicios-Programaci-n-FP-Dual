package casosTest;

import ejercicios.CuartoEjercicio;

public class CT_CuartoEjercicio {

	public static void main(String[] args) {
		
		//Caso TEST matrizUnaria
		int [][] matrizUnaria1 = new int[3][3];
		int [][] matrizUnaria2 = new int[4][3];
		int [][] matrizUnaria3 = new int[5][8];
		
		CuartoEjercicio.calcularMatrizUnaria(matrizUnaria1);
		CuartoEjercicio.calcularMatrizUnaria(matrizUnaria2);
		CuartoEjercicio.calcularMatrizUnaria(matrizUnaria3);
		
		CuartoEjercicio.imprimirMatrizUnaria(matrizUnaria1);
		CuartoEjercicio.imprimirMatrizUnaria(matrizUnaria2);
		CuartoEjercicio.imprimirMatrizUnaria(matrizUnaria3);
		

	}

}
