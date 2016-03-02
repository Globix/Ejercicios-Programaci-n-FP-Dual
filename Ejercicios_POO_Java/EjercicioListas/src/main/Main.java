package main;

import alumno.Alumno;
import colaErasmus.ColaErasmus;

public class Main {
	public static void main(String[] args) {
		
		// CASO TEST MOSTRAR ALUMNO
		System.out.println("CASO TEST MOSTRAR ALUMNO\n");
		
		Alumno alumno = new Alumno("Enrique", "Miranda", "Riquero");
		
		alumno.mostrarAlumno();

		// CASO TEST CREAR LISTA ALUMNOS Y MOSTRAR 1 a 1 LA COLA
		System.out.println("CASO TEST CREAR LISTA ALUMNOS Y MOSTRAR 1 a 1 LA COLA\n");
		
		ColaErasmus colaAlumnos = new ColaErasmus();

		String[][] casosAlumnos = { { "aitor", "lepe", "oyaga" }, { "victor", "santos", "algide" },
				{ "david", "mejide", "robles" } };

		for (String[] casoAlumno : casosAlumnos) {
			alumno = new Alumno(casoAlumno[0], casoAlumno[1], casoAlumno[2]);
			colaAlumnos.anyadirAlumno(alumno);
		}
		
		// MOSTRAMOS AHORA 1 a 1 LOS ALUMNOS INTRODUCIDOS
		
		for (int i = 0; i < colaAlumnos.tamanyoCola(); i++){
			colaAlumnos.mostrarPosicionColaIndex(i);
		}
		
		// CASO TEST MOSTRAR COLA
		System.out.println("CASO TEST MOSTRAR COLA\n");
		
		colaAlumnos.mostrarCola();
		
		// CASO TEST MOSTRAR TAMA�O COLA
		System.out.println("CASO TEST MOSTRAR TAMA�O COLA\n");
		
		colaAlumnos.mostrarTamanyoCola();
		
		// CASO TEST ADELANTAR ALUMNO EN LA COLA
		System.out.println("CASO TEST ADELANTAR ALUMNO EN LA COLA\n");
		
		colaAlumnos.adelantarAlumno(2, 0);
		colaAlumnos.mostrarCola();
		
		System.out.println("Probemos ahora buscando un rango fuera de la cola.\n");
		colaAlumnos.adelantarAlumno(5, 1);
		colaAlumnos.adelantarAlumno(2, 4);
		colaAlumnos.adelantarAlumno(-4, -5);
		
		// CASO TEST ELIMINAR ALUMNO DE LA COLA POR POSICION
		System.out.println("\nCASO TEST ELIMINAR ALUMNO DE LA COLA\n");
		
		colaAlumnos.eliminarAlumnoPosicion(1);
		colaAlumnos.mostrarCola();
		
		// CASO TEST MOSTRAR COLA INVERSA
		System.out.println("CASO TEST MOSTRAR COLA INVERSA\n");
				
		colaAlumnos.mostrarColaInversa();
		
		// CASO TEST LIMPIAR COLA
		System.out.println("CASO TEST LIMPIAR COLA\n");
		
		colaAlumnos.limpiarCola();
		
		System.out.println("Comprobamos ahora si la cola esta vacia ejecutando de nuevo mostrarCola.\n");
		colaAlumnos.mostrarCola();
		
		/*// CASO TEST ELIMINAR ALUMNO DE LA COLA POR ALUMNO
		System.out.println("CASO TEST ELIMINAR ALUMNO DE LA COLA POR ALUMNO\n");
		
		alumno = new Alumno("Enrique", "Miranda", "Riquero");
		
		colaAlumnos.anyadirAlumno(alumno);
		colaAlumnos.mostrarCola();
		
		System.out.println("-----------------------------------\n");
		
		alumno = new Alumno("aitor", "lepe", "oyaga");
		colaAlumnos.eliminarAlumno(alumno);
		colaAlumnos.mostrarCola();*/
		
	}
}