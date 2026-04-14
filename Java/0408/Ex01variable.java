package ex0408;

public class Ex01variable {
	// main 문을 실수로 만들지 않았을 때, main 이라고 한 다음 , ctrl + space
	public static void main(String[] args) {
		// 노란색 줄은 경고 -> 실행에는 아무 문제 없지만, 알림같은 서비스 
		int a = 10;
		System.out.println(a);
		// 상수 - 변하지 않는 수 , 모두 대문자로 작성
		//final 키워드를 사용
		final double PIE = 3.141592;
//		PIE = 20;// 상수는 바뀌지 않기 때문에 에러 발생.
		//기본타입 8가지
		//1. 논리형 - boolean
		//true / false 만 출력가능
		boolean b = true;
		System.out.println(b);
		
		//2. 문자형 - char (character)
		// 1개의 문자만 출력가능. ''로 표시
		char c= 'A';
		System.out.println(c);
		
		//3. 정수형 
		//byte, short, int, long
		//byte - 크기가 1byte -> 8bit 
		// 2의 8승 = 256 (-128 ~ 127)
//		byte by = 128; // 에러 발생 
		
		// 기본정수는 int
		long l = 100000L; //L은 생략가능
		
		//4. 실수형
		//float, double
		float f = 3.14f; 
		double d = 3.14; //뒷자리 d를 생략가능. 내부적으로 실수는 double로 판단
		
		//문자열 (문자형 - char)
		//String은 ""로 작성 - 키워드 X, 클래스
		String s = "hi";
		
		int num1 = 10;
		int num2 = 7;
		float num3 = 10.0f;
		float num4 = 7.0f;
		
		System.out.println(num1/num2);
		System.out.println(num3/num4);
		System.out.println(num1/num4); //int와 float를 계산하면 float로 나옴.
		
	}
}
