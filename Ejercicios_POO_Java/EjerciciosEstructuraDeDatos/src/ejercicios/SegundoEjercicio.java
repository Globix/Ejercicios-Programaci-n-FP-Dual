package ejercicios;

import java.util.concurrent.ThreadLocalRandom;

import main.Main;;

public class SegundoEjercicio {

	//Falta refactorizar bastantes cosas.
	public static void main(String[] args) {
		
		final int numeroMinimo = 25;
		final int numeroMaximo = 51;
		int[] lista = new int[25];
		double[] auxiliar = new double[4];
		//Inicializamos minimo con el n�mero m�ximo para que el primer numero que encuentre sea el m�s peque�o.
		int minimo = numeroMaximo;
		
		for (int i = 0; i < lista.length; i++){
			lista[i] = ThreadLocalRandom.current().nextInt(numeroMinimo, numeroMaximo);
		}
		
		for (int item:lista){
			if (item%2 == 0){
				auxiliar[0]++;
			}
			if (item%2 == 1){
				auxiliar[1]++;
				auxiliar[2] += item;
			}
			if (item < minimo){
				minimo = item;
			}
		}
		auxiliar[2] = auxiliar[2]/auxiliar[1];

		for (int i = 0; i < minimo; i++){
			auxiliar[3] += i;
		}
		
		for (int i = 0; i < lista.length; i++) {
            System.out.println("Posicion " + i + " de la lista = " + lista[i]);
        }
        System.out.println();

        System.out.println("Numero de elementos pares: " + (int)auxiliar[0]);
        System.out.println("Numero de elementos impares: " + (int)auxiliar[1]);
        System.out.println("Media impares: " + auxiliar[2]);
        System.out
                .println("Suma de lso enteros comprendidos entre 1 y el minimo de la lista: "
                        + auxiliar[3]);

        System.out.println("Fin del ejercicio");
		Main.main(null);
	}

}