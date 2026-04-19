package ex0413;

public class Ex03for {
	public static void main(String[] args) {
		
		//for (초기화 구문; 검사조건 ; 반복 후 작업){
		// 		실행문장
		//} 
		
		//1. 초기화 구문 실행. > 최초 1번만 실행
		//2. 검사 조건 -> true이면 반복
		//3. 실행문장
		//4. 반복 후 작업
		//5. 검사조건으로 -> 실행문장 -> 반복후 작업 .... (검사조건이 false까지)
		for(int i=0;i<=3;i++) {
			System.out.println("안녕하세요");
			System.out.println(i);
		}
		// 1~10 출력
		for(int i=1;i<=10;i++) {
			System.out.println(i);
		}
		System.out.println();
		// 21 ~ 53 출력
		for (int i=21;i<=53;i++) {
			System.out.println(i);
		}
		System.out.println();
		
		//96 ~ 57 까지 출력
		for (int i = 96;i>=57;i--) {
			System.out.print(i + " ");
		}
		System.out.println();
		
		//1부터 2씩 증가하는 수 (10까지만)
		for (int i=1;i<10;i+=2) {
			System.out.print(i + " ");
		}
		
		
		
		
		
	}
}
