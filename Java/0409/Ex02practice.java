package ex0409;

import java.util.Scanner;

public class Ex02practice {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Java 점수 입력 : ");
		int num1 = sc.nextInt();
		
		System.out.println("Web 점수 입력 : ");
		int num2 = sc.nextInt();
		
		System.out.println("Python 점수 입력 : ");
		int num3 = sc.nextInt();
		
		System.out.println("합계 : "+ (num1+num2+num3));
		System.out.println("평균 : "+(double)(num1+num2+num3)/3);
		System.out.println("평균 : "+(num1+num2+num3)/3.0);// 3.0으로 나눠버려도 됨.
	}
}
