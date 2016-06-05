package casosTest;
import java.util.LinkedList;
import java.util.Queue;

import alumno.Alumno;
import colaErasmus.ColaErasmus;

public class MainEjercicioListas {
	
	public static void main(String[] args) {
		Alumno alumno = new Alumno("Enrique", "Miranda", "Riquero");
		
		//CASO TEST MOSTRAR ALUMNO
		alumno.mostrarAlumno();
		
		ColaErasmus colaAlumnos = new ColaErasmus();
		
		//CASO TEST SACAR ALUMNOS 1 POR 1 POR ORDEN DE COLA
		
		String[][] casosAlumnos = {{"aitor", "algo", "lala"}, {"victor", "noob", "report"}, {"david", "kjash", "laks"}};
		
		for (String[] casoAlumno : casosAlumnos){
			alumno = new Alumno(casoAlumno[0], casoAlumno[1], casoAlumno[2]);
			colaAlumnos.anyadirAlumno(alumno);
			colaAlumnos.mostrarPosicionCola(alumno);
		}
		
		alumno = new Alumno("victor", "noob", "report");
		
		
	}
	
}