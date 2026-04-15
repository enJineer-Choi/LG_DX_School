package ex0409;

import java.util.Scanner;

//import jdk.internal.org.jline.terminal.TerminalBuilder.SystemOutput;

public class Ex01operator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//입력을 받아 두수의 합을 출력하는 결과
		
		//입력 받는 법 > 자동완성하는게 좋음!
		
		// 입력도구 생성!
		Scanner sc = new Scanner(System.in);
		// sc는 입력받는 도구
		System.out.println("첫 번째 숫자를 입력하세요 : ");
		
		
		// nextInt() > "숫자"만을 입력받게 함.
		int num1 = sc.nextInt();
		System.out.println("입력한 결과 값은 "+num1+"입니다.");
		
		
		
		System.out.println("두 번째 숫자를 입력하세요");
		int num2 = sc.nextInt();
		
		System.out.println("더한 결과 값 : " +(num1 + num2));
		System.out.println("뺀 결과 값 :" + (num1-num2));
		System.out.println("입력한 결과값은 " +num1*num2);
		System.out.println("입력한 결과값은 " +(double)num1/num2);
		
		//형변환 (casting) - 기본타입 8가지에만 적용
		//강제형변환 - 큰 타입이 작은 타입으로 변환 될 때 혹은 강제로 타입변환하고 싶을 때
		// 큰 타입 double -> 3.14 -> 작은 타입 int
		// (타입 작성) 변수
		// python에서는 int(input())
		//자동현변환 - 작은 타입이 큰 타입으로 변환 될 때
		System.out.println((double)(num1/num2));
	}

}
