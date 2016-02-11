package figuras;

public class Rectangulo extends FiguraGeometrica {
	
	private double base;
	private double altura;
	
	public Rectangulo(){
		super();
		base = 0;
		altura = 0;
	}
	
	public Rectangulo(String nombre){
		super(nombre);
		base = 0;
		altura = 0;
	}
	
	public Rectangulo(double base, double altura){
		this.base = base;
		this.altura = altura;
	}
	
	public Rectangulo(String nombre, double base, double altura){
		super(nombre);
		this.base = base;
		this.altura = altura;
	}

	public double getBase() {
		return this.base;
	}

	public void setBase(double base) {
		this.base = base;
	}

	public double getAltura() {
		return this.altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}
	
	@Override
	public double calcularArea(){
		double area = this.base * this.altura;
		return area;
	}

	@Override
	public String toString() {
		return "Rectangulo [nombre=" + super.getNombre() + ", area=" + calcularArea() + "]";
	}

}
