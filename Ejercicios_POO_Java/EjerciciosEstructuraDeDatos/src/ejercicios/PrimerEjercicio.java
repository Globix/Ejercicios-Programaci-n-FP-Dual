package ejercicios;

import main.Main;

public class PrimerEjercicio {

	public static void main(String[] args) {
		
		double[] venta = {50, 24, 16, 789, 35};
		
		System.out.println("Bienvenido al ejercicio 1\n");
		
		calcularVentas(venta);
		
		System.out.println("Fin del ejercicio\n");
		Main.main(null);
	}
	
	public static void calcularVentas(double[] venta){
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
