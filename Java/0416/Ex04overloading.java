package ex0416;

public class Ex04overloading {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println();
	}
	//매개변수의 합을 구하는 메소드 
	public static void sum1(int num1, int num2) {
		System.out.println(num1+num2);
	}
	
	//만약 내가 int와 double을 더하는 메소드를 만들고 싶음
	// 그러면 새롭게 만들어야함
	// 메소드의 오버로딩 (메소드의 중복정의)
	
	//조건 1 : 메소드의 이름을 같게 할 것!
	//조건 2 : 매개변수의 개수나 타입이 서로 달라야 함.
	// 참고 : 리턴 타입이랑 접근지정자는 관련이 없음
	public void sum1() {
		
	}
	
	
}
