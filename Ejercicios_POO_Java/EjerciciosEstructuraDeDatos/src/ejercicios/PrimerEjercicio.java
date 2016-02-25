package ejercicios;

import main.Main;

public class PrimerEjercicio {

	public static void main(String[] args) {
		
		double[][] ventas = {{50, 24, 16, 789, 35},
						  {4566, 2356, 72.45, 12.2, 67},
						  {1, 1, -4, 3, 4}};
		
		for (double[] venta:ventas){
			calcularVentas(venta);
		}
		System.out.println("Fin del ejercicio");
		Main.main(null);
	}
	
	private static void calcularVentas(double[] venta){
		double mayorVenta = venta[0];
		double menorVenta = venta[0];
		double totalVenta = 0;
		
		for (double ventaTienda:venta){
			if (ventaTienda > mayorVenta){
				mayorVenta = ventaTienda;
			}
			if (ventaTienda < menorVenta){
				menorVenta = ventaTienda;
			}
			if (ventaTienda > 0){
				totalVenta += ventaTienda;
			}
		}
		
		System.out.println("La mayor venta de todas las tiendas fue: " + mayorVenta + "�");
		System.out.println("La menor venta de todas las tiendas fue: " + menorVenta + "�");
		System.out.println("El total de ventas entre todas las tiendas fue: " + totalVenta + "�\n");
	}

}