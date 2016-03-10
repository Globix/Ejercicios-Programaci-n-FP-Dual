package figuras;

public abstract class FiguraGeometrica implements draw.Drawable {
	
	private String nombre;
	
	public FiguraGeometrica(){
		this.nombre = "SinAsignar";
	}
	
	public FiguraGeometrica(String nombre){
		this.nombre = nombre;
	}

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public abstract double calcularArea();

	//public abstract void draw();
}
