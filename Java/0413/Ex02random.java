package ex0413;

import java.util.Random;
import java.util.Scanner;

public class Ex02random {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// up down 게임만들기
		// 1.랜덤 난수 뽑기 (1~50)
		// 2. 숫자 입력 
		// 3. 난수와 비교하여 업/다운을 출력
		// 4. 난수와 입력값이 일치하면 종료
		
		
		// 1.랜덤 난수 생ㅅ성
		Random r = new Random();
		
		int random_num = r.nextInt(50)+1;
		//nextInt안에 주는 숫자는 범위 지정 (0부터 시작)
//		System.out.println(random_num);
		
		// 2. 숫자입력 > 정답을 맞출 때까지 입력
		Scanner sc = new Scanner(System.in); 
		// new하면은 메모리에 지속적으로 저장되는데, 반복문 안에 존재하면
		// 새로 정수를 받을 때마다 계속 저장됨
		// 입력할때마다 1씩 증가하는 변수
		int cnt = 0;
		do {
			System.out.println("숫자 입력 : ");
			int num1 = sc.nextInt();
			cnt++;
			// 난수와 비교하기
			if (num1 < random_num) {
				System.out.println("더 큰 수 입니다");
			}else if (num1 > random_num) {
				System.out.println("더 작은 수 입니다");
			}else {
				System.out.println(cnt + "번 만에 정답입니다!");
				break;
			}
			
		} while (true);
		
		
//		do {
//			Scanner sc = new Scanner(System.in);
//			int num = sc.nextInt();
//			
//		} while (num == random_num); >이렇게 코드를 작성하면 안됨...
		
		
		
	}

}
	