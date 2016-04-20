package roverTest;

import static org.junit.Assert.*;
import rover.Rover;
import java.awt.Point;

import org.junit.BeforeClass;
import org.junit.Test;

public class RoverTest {
	
	static Rover rover;
	double x;
	double y;
	Point coordinates;
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		rover = new Rover();
		rover.setCoordinates(4, 5);
		rover.printPosition();
	}


	@Test
	public void testMove() {
		fail("Not yet implemented");
	}

	@Test
	public void testMoveForward() {
		coordinates = rover.getCoordinates();
		x = coordinates.getX();
		y = coordinates.getY() + 1;
		Point expected = new Point();
		expected.setLocation(x, y);	
		rover.moveForward(coordinates);
		assert (coordinates == expected);
		rover.printPosition();
	}

	@Test
	public void testMoveBackward() {
		coordinates = rover.getCoordinates();
		x = coordinates.getX();
		y = coordinates.getY() - 1;
		Point expected = new Point();
		expected.setLocation(x, y);	
		rover.moveBackward(coordinates);
		assert (coordinates == expected);
		rover.printPosition();
	}

	@Test
	public void testChangeDirectionLeft() {
		fail("Not yet implemented");
	}

	@Test
	public void testChangeDirectionRight() {
		fail("Not yet implemented");
	}

}
