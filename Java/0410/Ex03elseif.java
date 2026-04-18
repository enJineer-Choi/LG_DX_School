package ex0410;

import java.util.Scanner;

public class Ex03elseif {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//python에서의 elif = else if 
		Scanner sc = new Scanner(System.in);
		System.out.println("점수 입력 : ");
		int totalscore = sc.nextInt();
		
//		int num1 = 10;
		if (totalscore >= 90) {
			System.out.println("A학점입니다");
		}else if (totalscore >= 80) {
			System.out.println("B학점입니다");
		}else if (totalscore >=70) {
			System.out.println("C학점입니다");
		}else {
			System.out.println("D학점입니다");
		}
	}

}



