package casosTest;

import ejercicios.PrimerEjercicio;

public class CT_PrimerEjercicio {

	public static void main(String[] args) {

		//Casos TEST calcularVentas
		double[][] ventas = {{50, 24, 16, 789, 35},
				  {4566, 2356, 72.45, 12.2, 67},
				  {1, 1, -4, 3, 4}};

		for (double[] venta:ventas){
			PrimerEjercicio.calcularVentas(venta);
		}

	}

}
