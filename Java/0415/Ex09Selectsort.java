package ex0415;

import java.util.Arrays;

public class Ex09Selectsort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 내림차순 정렬

		// 1step : max = 0, max <1,max<2,max<3,max<4 -> 0번째와 치환
		// 2step : max = 1, max<2,max<3,max4
		int[] array = { 7, 98, 13, 70, 24 };
//		int max = array[0];
//		int max_index = 0;
//		for (int i = 1; i < array.length; i++) {
//			if (array[max_index] < array[i]) {
//				max_index = i;
//			}
//		}
//		int temp = array[0];
//		array[0] = array[max_index];
//		array[max_index] = temp;
//
//		System.out.println(Arrays.toString(array));

//		for (int j = 0; j < array.length-1; j++) { // array.length-1까지만 해도 됨 (3까지만 하면 되니깐)
//			int max_index = j;
//			for (int i = j+1; i < array.length; i++) {// i=j+1 부터 시작해야함? ㅇㅇ
//				if (array[max_index] < array[i]) {
//					max_index = i;
//				}
//			}
//			int temp = array[j];
//			array[j] = array[max_index];
//			array[max_index] = temp;
//			
//			System.out.println(Arrays.toString(array));
//		}
//		
		//오름차순
		for (int j=0;j<array.length-1;j++) {
			
			int min_index = j;
			for (int i=j+1;i<array.length;i++) {
				if(array[min_index]>array[i]) {
					min_index = i;
				}
			}
			int temp = array[j];
			array[j] = array[min_index];
			array[min_index] = temp;
			
			System.out.println(Arrays.toString(array));
		}
	}

}
