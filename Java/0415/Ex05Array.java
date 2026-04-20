package ex0415;

public class Ex05Array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr1 = new int[5];
		
		arr1[0] = 12;
		arr1[1] = 45;
		arr1[2] = 37;
		arr1[3] = 8;
		arr1[4] = 62;
		
		
		//arr1 -> (정수형) 배열 
		//arr1[0] -> int
		
		System.out.println(arr1[0]+arr1[3]);
		//arr1자체 (arr1은 배열타입) 와 arr1이 담고 있는 값 (arr1[0]은 int) 은 다름.
		
		
		String arr2[] = new String[3];
		arr2[0] = "홍길동";
		arr2[1] = "이순신";
		arr2[2] = "허준";
		
		//arr2는 (문자열) 배열
		//arr2[]요소는 String (문자열)
		
	}

}
