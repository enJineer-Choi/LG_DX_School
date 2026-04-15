package ex0409;

public class Ex03and {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 10;
		int b = 20;
		
		// 논리 연산자의 단축평가
		// && 연산자의 경우 두 항이 모두 true 이어야만 결과값이 true
		//A && B A-false 이면 B의 값은 중요하지 않음.. > 그래서 B를 실행하지 않음
		if (a > 20 && ++b > 30) {
			// 실행 안됨
		}
		System.out.println("b: " + b);
		
		
		// or (A||B) -> A가 true 이면 어차피 값은 true
		// B가 true/false 상관없이 (A||B) -> true
		// B를 실행하지 않습니다
		if (a < 20 || ++b > 30) {
			System.out.println("참입니다.");
		}
	}

}
