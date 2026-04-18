package ex0410;

import java.util.Scanner;

public class Ex09string {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("계속 하시겠습니까?");
			//y를 누르면 반복, n을 누르면 반복 종료
			//문자를 입력받는 법
			String s = sc.next();
			
			// 클래스는 레퍼런스 (주소값)을 저장.
			// 즉 s객체는 현재 주소값을 저장하므로, == 을 통해서 비교하면 주소값과
			//"n"이라는 문자열을 비교하는 것.
			
			//그래서 String이 값이 같은지를 비교하려면
			//.equals()를해야함
//			if(s=="n") 
			if(s.equals("n")){ // ==: 값을 비교하는 연산자
				System.out.println("종료");
				break;
			}
		}
	}

}
