package expresionRegular;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class ExpresionRegular {
	
	private Pattern expresionRegular;
	
	public ExpresionRegular(){
		this.expresionRegular = null;
	}
	
	public ExpresionRegular(String expresionRegular){
		this.expresionRegular = Pattern.compile(expresionRegular);
	}
	
	public void setExpresionRegular(String expresionRegular){
		this.expresionRegular = Pattern.compile(expresionRegular);
	}
	
	public Pattern getExpresionRegular(){
		return expresionRegular;
	}
	
	public void comprobarSano(String expresionAComprobar){
		Matcher m;
		boolean sano;
		m = expresionRegular.matcher(expresionAComprobar);
		sano = m.matches();
		
		if (sano == true){
			System.out.println("La expresión sigue la Reglas establecidas");
		} else {
			System.out.println("La expresión no sigue las Reglas establecidas");
		}
	}
	
	
}
