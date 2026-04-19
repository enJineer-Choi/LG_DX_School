package ex0413;

import java.util.Scanner;

public class Ex08divide {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("정수 입력 : ");
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for (int i = 1; i<=num;i++) {
			if(num%i==0) {
				System.out.print(i+" ");
			}
		}
	}

}
