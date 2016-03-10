package test;

import java.util.ArrayList;
import java.lang.UnsupportedOperationException;

import org.junit.Test;

import figuras.*;
import draw.Drawables;

public class DrawableTest {

	@Test
	public void testDraw() {
		ArrayList<FiguraGeometrica> figuras = new ArrayList<>();

		Rectangulo rectanguloCompleto = new Rectangulo("Rectangulo4", 4, 5);

		Circulo circuloCompleto = new Circulo("Circulo4", 4);

		Cuadrado cuadradoCompleto = new Cuadrado("Cuadrado4", 4);

		Elipse elipseCompleto = new Elipse("Elipse4", 3, 5);

		figuras.add(rectanguloCompleto);
		figuras.add(circuloCompleto);
		figuras.add(cuadradoCompleto);
		figuras.add(elipseCompleto);

		Drawables.drawAll(figuras);
		Drawables.applyTheme(figuras);

	}

}
