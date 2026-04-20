package ex0415;

public class Ex07Array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 레퍼런스 변수 선언 -> 주소값을 저장
		int [] array;
		
		//배열 생성
		array = new int[5];
		
		int [] array2 = array;
		array2[2] = 3;
		System.out.println(array2[2]);
		System.out.println(array[2]);
		// 주소를 복사해왔기 때문에 둘이 값이 똑같이 만들어짐.
		System.out.println(array);
		System.out.println(array2);
		
		
		int num = 10;
		int num1 = num;
		
		num = 7;
		System.out.println(num1);
		//기본 데이터 타입은 값자체를 복사해오기 때문에, 같은 주소를 가리키고 있지 않음. 
		// 그래서 기존 값을 바꿔도 값이 바뀌지 않음
	}

}
