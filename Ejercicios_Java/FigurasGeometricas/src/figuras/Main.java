package figuras;

import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
		ArrayList<FiguraGeometrica> figuras = new ArrayList<>();
		
		Rectangulo rectanguloVacio = new Rectangulo();
		Rectangulo rectanguloConNombre = new Rectangulo("Rectangulo2");
		Rectangulo rectanguloConMedidas = new Rectangulo(6,5);
		Rectangulo rectanguloCompleto = new Rectangulo ("Rectangulo4", 4, 5);
		
		Circulo circuloVacio = new Circulo();
		Circulo circuloConNombre = new Circulo("Circulo2");
		Circulo circuloConMedidas = new Circulo(6);
		Circulo circuloCompleto = new Circulo ("Circulo4", 4);
		
		Cuadrado cuadradoVacio = new Cuadrado();
		Cuadrado cuadradoConNombre = new Cuadrado("Cuadrado2");
		Cuadrado cuadradoConMedidas = new Cuadrado(6);
		Cuadrado cuadradoCompleto = new Cuadrado ("Cuadrado4", 4);
		
		Elipse elipseVacio = new Elipse();
		Elipse elipseConNombre = new Elipse("Elipse2");
		Elipse elipseConMedidas = new Elipse(2,4);
		Elipse elipseCompleto = new Elipse ("Elipse4", 3, 5);
		
		figuras.add(rectanguloVacio);
		figuras.add(rectanguloConNombre);
		figuras.add(rectanguloConMedidas);
		figuras.add(rectanguloCompleto);
		figuras.add(circuloVacio);
		figuras.add(circuloConNombre);
		figuras.add(circuloConMedidas);
		figuras.add(circuloCompleto);
		figuras.add(cuadradoVacio);
		figuras.add(cuadradoConNombre);
		figuras.add(cuadradoConMedidas);
		figuras.add(cuadradoCompleto);
		figuras.add(elipseVacio);
		figuras.add(elipseConNombre);
		figuras.add(elipseConMedidas);
		figuras.add(elipseCompleto);
		
		for (FiguraGeometrica figura: figuras){
			System.out.println(figura.toString());
		}
		
		

	}

}
