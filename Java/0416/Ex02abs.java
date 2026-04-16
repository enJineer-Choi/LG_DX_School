package ex0416;

import java.util.Scanner;

public class Ex02abs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//키보드로부터 입력받은 두개의 정수를 인자로 넘겨받아 num1에서 num2를 뺀값을 절댃값으로 바꾸는 메소드ㅜ
		Scanner sc = new Scanner(System.in);
	
		System.out.println("첫번째 숫자를 입력하세요 : ");
		int num1 = sc.nextInt();
		System.out.println("두번째 숫자를 입력하세요 : ");
		int num2 = sc.nextInt();
		
		int result = abs(num1,num2);
		System.out.println("뺀 결과값 : "+result);
		
	}
	public static int abs(int a, int b) {
		// 1. a,b 비교 해서 더 큰수 - 작은수
		
//		if(a>b) {
//			return a-b;
//		}else {
//			return b-a;
//		}
		
		// 2. a,b 뺀 후에 음수면 * -1
		
		int result = a-b;
		if (result<0) {
//			result *= -1;
			result = -result;
		}
		return result;
	
	}

}
