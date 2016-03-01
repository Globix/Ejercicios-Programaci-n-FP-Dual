package ejercicios;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

import main.Main;

public class TercerEjercicio {

	public static void main(String[] args) {

		final int numeroRangoMinimo = 1;
		final int numeroRangoMaximo = 20;
		int[] lista = new int[30];

		System.out.println("Bienvenido al ejercicio 3\n");

		lista = numerosAleatorios(numeroRangoMinimo, numeroRangoMaximo, lista);
		Arrays.sort(lista);
		imprimirLista(lista);

		System.out.println("Fin del ejercicio\n");
		Main.main(null);
	}

	public static int[] numerosAleatorios(int numeroRangoMinimo, int numeroRangoMaximo, int[] lista) {

		for (int i = 0; i < lista.length; i++) {
			lista[i] = ThreadLocalRandom.current().nextInt(numeroRangoMinimo, numeroRangoMaximo);
		}

		return lista;
	}

	public static void imprimirLista(int[] lista) {

		for (int i = 0; i < lista.length; i++) {
			System.out.println("Posicion " + i + " de la lista = " + lista[i]);
		}
		System.out.println();
	}

}
