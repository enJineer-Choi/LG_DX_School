package ex0416;

public class Ex05Car_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 객체 생성 키워드 new
		// 객체 생성 방법 : 클래스명 변수명 = new 클래스명
		Ex05Car hyundai = new Ex05Car();
		
		//해당 객체에 있는 필드와 메소드 접근 가능
		hyundai.speedUp();
		// . 을 해석할 때, hyundai의 speedUp()을 구현하겠다라고 이해하면 쉬움
	}

}
