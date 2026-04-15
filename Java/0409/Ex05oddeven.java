package ex0409;

import java.util.Scanner;

public class Ex05oddeven {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//삼항 연산자 사용하여 간단한 짝수 / 홀수 구하는 예제
		Scanner sc = new Scanner(System.in);
		
		System.out.println("정수를 입력 : ");
		int num1 = sc.nextInt();
		
		// 짝수인지 홀수인지
		String result = num1 % 2 == 0 ? "짝수" : "홀수" ;
		System.out.println(num1+"은 "+result+"입니다");
	}

}
