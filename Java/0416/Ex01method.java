package ex0416;

public class Ex01method {

	public static void main(String[] args) {
		//main문도 메소드의 일종 (매개변수는 String 배열)
		// TODO Auto-generated method stub	
		//메소드 호출
		addNum1();
		// 현재 에러가 난 이유 : addNum1()이 static이 아니어서 에러 발생
		addNum2(10,11);
		int result = addNum3(); //addNum3()은 타입이 존재! -> int(return 과 동일)
		// 호출해도 print되지 않음.
		// type이 int형이므로 변수에 대입이 가능함!!!
		System.out.println(result);
		
		System.out.println(addNum4(10,11));
		//출력문 안에 바로 메소드 넣어주는 것도 가능!
		//매개변수는 순서에 맞춰서 들어가게 됨
		
	}
	// 1. 메소드 작성법 - 매개변수 X / 리턴 X
	public static void addNum1() {
		System.out.println(10+11);
	}
	
	// 3. 메소드 작성법 - 매개변수 X / 리턴 O > 반드시 return 키워드와 같이 와야함
	public static int addNum3() {
		return 10+11;
		//리턴 키워드는 반복문 , 메소드를 종료하는 키워드 (return 밑에 코드를 작성하면 안됨)
	}
	
	
	// 2. 메소드 작성법 - 매개변수 O / 리턴 X
	public static void addNum2(int num1, int num2) {

		int result = num1 + num2;
		System.out.println(result);
	}
	
	// 4. 메소드 작성법 - 매개변수 O / 리턴 O
	public static int addNum4(int num1, int num2) {
		return num1 + num2;
	}

}
