package ex0416;

public class Ex05Car {
	// 클래스란 설계도 -> 객체 생성
	// 필드 (변수) - 해당 클래스(설계도)가 가지고 있는 속성 
	String handle;
	int speed;
	String nav;
	String color;
	int hp;
	int rpm;
	
	
	// 메소드 - 해당 클래스가 가지고 있는 기능
	public void speedUp() {
		speed++;
	}
	public void speedDown() {
		speed--;
	}
	
}
