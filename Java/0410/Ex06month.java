package ex0410;

import java.util.Scanner;

public class Ex06month {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("월 입력:");
		int month = sc.nextInt();
		
		switch (month) {
		case 4,6,9,11:
			System.out.println(month+"월의 날수는 30일 입니다");
			
			break;
		case 2:
			System.out.println(month+"월의 날수는 28일 입니다");
			break;
		case 1,3,5,7,8,10,12:
			System.out.println(month+"월의 날수는 31일 입니다");
			break;
		default:
			System.out.println("월을 잘못 입력하셨습니다");
			break;
		}
	}
}
