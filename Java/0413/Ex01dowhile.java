package ex0413;

import java.util.Scanner;

public class Ex01dowhile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//do while 문
		// do : 일단 한번 실행해라
		// 일반 while문은 true일때만 반복이 진행
		// do-while문은 일단 한번 실행하고 true이면 반복
		// 10이상의 수를 입력받아 
		Scanner sc = new Scanner(System.in);
		do {
			
			System.out.println("정수입력 : ");			
			int num1 = sc.nextInt();
			
			if (num1>=10) {
				System.out.println("종료 되었습니다.");
				break;
			}
		} while (true);
	}

}
