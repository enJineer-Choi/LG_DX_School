package ex0413;

public class Ex09multi {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 다중반복문 : 반복문 안에 반복문
		
		for (int i=0;i<=3;i++) {
			// i는 지역변수 이므로 for문 안에서만 사용할 수 있음.
			for (int j=0;j<=3;j++) {
				System.out.println("i의 결과값 : "+i);
				System.out.println("j의 결과값 : "+j);
				
			}
			System.out.println("i의 결과 값 22 : "+ i);
		}
		
	}

}
