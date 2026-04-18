package ex0410;

import java.util.Scanner;

public class Ex08num {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			System.out.println("정수입력 : ");
			int num1 = sc.nextInt();
			
			if (num1>=10) {
				System.out.println("종료되었습니다");
				break;
			}
		}
		sc.close(); //scanner 닫기 코드
	}

}
