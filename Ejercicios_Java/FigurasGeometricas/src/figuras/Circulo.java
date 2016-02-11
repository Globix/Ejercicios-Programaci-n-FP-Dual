package figuras;

public class Circulo extends FiguraGeometrica {
	
	private double radio;
	
	public Circulo (){
		super();
		radio = 0;
	}
	
	public Circulo (String nombre){
		super(nombre);
		radio = 0;
	}
	
	public Circulo (double radio){
		super();
		this.radio = radio;
	}
	
	public Circulo (String nombre, double radio){
		super(nombre);
		this.radio = radio;
	}

	public double getRadio() {
		return this.radio;
	}

	public void setRadio(double radio) {
		this.radio = radio;
	}
	
	@Override
	public double calcularArea(){
		double area = Math.sqrt(radio * Math.PI);
		return area;
	}
	
	@Override
	public String toString() {
		return "Circulo [nombre=" + super.getNombre() + ", area=" + calcularArea() + "]";
	}

}
