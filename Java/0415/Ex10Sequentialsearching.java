package ex0415;

import java.util.Arrays;
import java.util.Scanner;

public class Ex10Sequentialsearching {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] array = {13,35,15,11,27,72,78,13,61,90};
		
		
		int num = 78;
		int num_index = 0;
		for (int i = 0;i<array.length-1;i++) {
			if(num == array[i]) {
				num_index = i;
			}
		}
		System.out.println(Arrays.toString(array));
		System.out.println(num+"은(는) "+ num_index+"번째 숫자입니다.");
		
		//만약 입력받아서 한다면 
		Scanner sc = new Scanner(System.in);
		System.out.println("숫자를 입력해 주세요 : ");
		int num1 = sc.nextInt();
		int num1_index = 0;
		for (int i = 0;i<array.length-1;i++) {
			if(num1 == array[i]) {
				num1_index = i;
				break; // 더이상 반복하지 않고 싶으면 break로 반복을 끝내기
			}
			
		}
		System.out.println(Arrays.toString(array));
		System.out.println(num1+"은(는) "+ num1_index+"번째 숫자입니다.");
		
	}

}
