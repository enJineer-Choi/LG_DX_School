package ex0409;

import java.util.Scanner;

public class Ex06bignumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		System.out.println("첫번째 수를 입력해주세요");
		int num1 = sc.nextInt();
		
		System.out.println("두번째 수를 입력해주세요");
		int num2 = sc.nextInt();
		
		int result = num1 > num2 ? num1 - num2 : num2 - num1;
		
		System.out.println("결과값은 "+ result + "입니다");
	}

}
