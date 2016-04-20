package rover;

import java.awt.Point;

public class Rover {
	
	private Point coordinates;
	private Direction direction;
	
	public Rover(){
		this.coordinates.setLocation(0, 0);
		this.direction = Direction.NORTH;
	}
	
	public Rover(int x, int y, Direction direction){
		this.coordinates.setLocation(x, y);
		this.direction = direction;
	}

	public Point getCoordinates() {
		return this.coordinates;
	}

	public void setCoordinates(int x, int y) {
		this.coordinates = new Point(x, y);
	}
	
	public void move(char command) throws Exception {
        switch(Character.toUpperCase(command)) {
            case 'F':
                moveForward(coordinates);
            case 'B':
                moveBackward(coordinates);
            case 'L':
                changeDirectionLeft(coordinates);
            case 'R':
                changeDirectionRight(coordinates);
            default:
                throw new Exception("Command " + command + " is unknown.");
        }
    }
	
	public void printPosition() {
        Point coordinates = getCoordinates();
        System.out.println("El robot esta en: " + coordinates.getX() + ", "+ coordinates.getY());
    }
	
	public void moveForward(Point coordinates){	
		double x = coordinates.getX();
		double y = coordinates.getY();
	    Direction direction;
		coordinates.setLocation(x, y);
	}
	
	public void moveBackward(Point coordinates){
		double x = coordinates.getX();
		double y = coordinates.getY();
		coordinates.setLocation(x, y - 1);
	}

	public void changeDirectionLeft(Point coordinates){	
	}
	
	public void changeDirectionRight(Point coordinates){	
	}
}
