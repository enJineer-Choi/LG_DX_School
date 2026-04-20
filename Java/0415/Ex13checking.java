package ex0415;

import java.util.Scanner;

public class Ex13checking {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 채점 프로그램 
		int [] answer = {1,4,3,2,1};
		int [] array = new int[5];
		
		System.out.println("==채점하기==");
		System.out.println("답을 입력하세요");
		for (int i = 0;i<array.length;i++) {
			Scanner sc = new Scanner(System.in);
			System.out.print(i+1 +"번답 >> ");
			array[i] = sc.nextInt();
			
		}
		System.out.println("정답확인");
		
		int score = 0;
		for (int i =0;i<array.length;i++) {
			if(answer[i] == array[i]) {
				System.out.print("O"+"  ");
				score +=20;
			}else {
				System.out.print("X"+"  ");
			}
		}
		System.out.print("총점 : " + score);
		
	}

}
