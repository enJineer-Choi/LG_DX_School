package ex0415;

public class Ex06Array_practice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//배열의 값중 가장 큰값과 가장 작은 값을 출력
		int [] arr1 = {2, 10, 3, 5, 56, 41, 7, 18, 94};
		
		
		//가장 큰값 출력
		int max = arr1[0];
		
		for (int i = 0;i<arr1.length;i++) { 
			//i<=arr1.length로 반복문을 생성하면 i의 범위가 벗어나게 됨.
			//이유 > for문의 실행 순서 때문에, 반복문이 다 돌고 또 올라가서 i<arr1.length를 비교를 하게 됨.
			if(max<=arr1[i]) {
				max = arr1[i];
			}
		}
		System.out.println("가장 큰 값은 " + max);
		// 가장 작은 값
		int min = arr1[0];
		
		for (int i = 0;i<arr1.length;i++) { 
			//i<=arr1.length로 반복문을 생성하면 i의 범위가 벗어나게 됨.
			//이유 > for문의 실행 순서 때문에, 반복문이 다 돌고 또 올라가서 i<arr1.length를 비교를 하게 됨.
			if(min>=arr1[i]) {
				min = arr1[i];
			}
		}
		System.out.println("가장 큰 값은 " + min);
		
		
	}

}
