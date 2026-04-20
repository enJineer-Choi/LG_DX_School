package ex0415;

import java.util.Arrays;

public class Ex08bubblesort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 오름차순 정렬
		int [] array = {10,7,6,3,1};
		//1step : [0,1] [1,2] [2,3] [3,4]
		//2step : [0,1] [1,2] [2,3] 
		//3step : [0,1] [1,2] 
		//4step : [0,1] 
		
		
		//1step 
		for (int i = 0;i<array.length-1;i++) {
			if(array[i]>array[i+1]) {
				int temp = array[i];
				array[i]=array[i+1];
				array[i+1] = temp;
			}
			
		}
		//배열안의 데이터를 한꺼번에 출력하는 법
		System.out.println(Arrays.toString(array));
		// 코드를 이렇게 짜면 out of bound 에러 발생
		//array.length-1을 해줘야 배열의 범위를 벗어나지 않음
		// 이렇게 코드를 짜면 10이 계속 중복되서 들어가게 됨.
		// 임시값을 저장할 temp 변수를 만들어줘야함! > 안그러면 계속 값이 누적해서 싸임.
		
		
		// 전체 스텝 1번에 작성 
		for (int j =1;j<array.length;j++) {
			for (int i = 0;i<array.length-j;i++) {
				if(array[i]>array[i+1]) {
					int temp = array[i];
					array[i]=array[i+1];
					array[i+1] = temp;
				}
				
			}
		}
		System.out.println(Arrays.toString(array));
		
		
		
		// 내림차순 정렬 
		int [] array1 = {1,3,6,8,10};
		for (int i = 0;i<array.length-1;i++) {
			if(array1[i]<array1[i+1]) {
				int temp = array1[i+1];
				array1[i+1] = array1[i];
				array1[i] = temp;
			}
		}
		System.out.println(Arrays.toString(array1));
		
		for (int j = 1;j<array1.length;j++) {
			for (int i = 0;i<array.length-1;i++) {
				if(array1[i]<array1[i+1]) {
					int temp = array1[i+1];
					array1[i+1] = array1[i];
					array1[i] = temp;
				}
			}
		}
		System.out.println(Arrays.toString(array1));
		
		
	}

}
