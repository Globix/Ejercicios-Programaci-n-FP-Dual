package figuras;

public class Cuadrado extends FiguraGeometrica {
	
	double lado;
	
	public Cuadrado(){
		lado = 0;
	}
	
	public Cuadrado(String nombre){
		super(nombre);
		lado = 0;
	}
	
	public Cuadrado(double lado){
		this.lado = lado;
	}
	
	public Cuadrado(String nombre, double lado){
		super(nombre);
		this.lado = lado;
	}

	public double getLado() {
		return this.lado;
	}

	public void setLado(double lado) {
		this.lado = lado;
	}
	
	@Override
	public double calcularArea(){
		double area = lado * lado;
		return area;
	}
	
	@Override
	public String toString() {
		return "Cuadrado [nombre=" + super.getNombre() + ", area=" + calcularArea() + "]";
	}
	
	
}
