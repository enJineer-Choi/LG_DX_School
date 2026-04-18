package ex0410;

import java.util.Scanner;

public class Ex01conditional {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 단순 if문
		
		if (10<20) {// 조건문 안에 true라고만 작성해도 가능함
			System.out.println("더 큽니다!");
		}
		// 나이를 ㅣㅂ력받고 20살 이상이면 성인입니다 출력
		Scanner sc = new Scanner(System.in);
		System.out.println("나이를 입력하세요:");
		int age = sc.nextInt();
		
		if (age>=20) {
			System.out.println("성인입니다");
		}
	}

}
