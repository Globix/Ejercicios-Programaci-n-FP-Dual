package draw;

import java.util.ArrayList;

import figuras.FiguraGeometrica;

public class Drawables {
	public static void drawAll(ArrayList<FiguraGeometrica> figuras) {
		for (FiguraGeometrica figura : figuras) {
			figura.draw();
		}
	}

	public static void applyTheme(ArrayList<FiguraGeometrica> figuras) {
		for (FiguraGeometrica figura : figuras) {
			try {
				figura.applyTheme();
			} catch (UnsupportedOperationException e) {
				System.out.println("applyTheme no aplicado");
			}
		}
	}
}
