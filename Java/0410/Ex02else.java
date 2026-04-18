package ex0410;

import java.util.Scanner;

public class Ex02else {
	public static void main(String[] args) {
		//if - else
		//20살 이상이면 성인입니다 출력, 아니면 성인이 아닙니다 출력
		Scanner sc = new Scanner(System.in);
		System.out.println("나이를 입력해주세요 : ");
		int age = sc.nextInt();
		
		if (age > 20) {
			System.out.println("성인입니다");
		}else{
			// else 뒤에는 조건식이 따로 없음
			System.out.println("성인이 아닙니다");
		}
	}
}

// 정렬 단축키 : ctrl + shift + f