package ex0415;

public class Ex04array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 배열 Array
		// 리스트와 공통점
		// - 인덱스로 대응 -> 인덱스로 데이터 접근
		// - 0번부터 시작
		// - 같은 타입의 데이터를 저장
		// - 사전에 크기를 지정(회원가입 등 가변성 있는 데이터에는 적합하지 않음)
		// - 위 단점을 해결하기 위해 ArrayList

		// 배열 선언
		// 자료형 혹은 변수명 뒤에 [] 넣기
		int[] arr1 = new int[3];
		// new -> 객체 생성 키워드
		System.out.println(arr1); // reference의 주소값이 출력됨.

		// 대괄호 사용해서 인덱스로 출력가능
		System.out.println(arr1[0]); // 0이 출력됨.
		// 기본타입 8가지는 미작성시 기본값이 0임
		// boolean의 기본값 0 (false)

		arr1[0] = 10;
		arr1[1] = 20;
		arr1[2] = 30;

		System.out.println(arr1[0]);
		System.out.println(arr1[1]);
		System.out.println(arr1[2]);

		System.out.println();
		// 에러 > Index Out Of Bounds Exception (범위 밖 에러)
//		arr1[3] = 40;
		// 맞지 않는 범위 값을 출력하려고 할 때 발생하는 에러

		// Error에는 2가지 에러가 존재
		// 1. compile error -> 빨간줄 (문법 오류)
		// 2. runtime error -> 실행해야 오류인지 아닌지 알수 있는 에러 (코드상 문법에 에러가 없음)

		// 반복문을 활용한 출력
		for (int i = 0; i < 3; i++) {
			System.out.println(arr1[i]);
		}

		System.out.println();

		// 3대신 arr1의 길이를 활용하여 반복문 실행
		for (int i = 0; i < arr1.length; i++) {
			System.out.println(arr1[i]);
		}
		System.out.println();

		// for-each문을 활용
		for (int num1 : arr1) {
			System.out.println(num1);
		}
		System.out.println();

		// 배열생성과 동시에 값 초기화
		int[] arr2 = { 100, 200, 300 };

		// 반복문 활용하여 출력
		for (int i = 0; i < arr2.length; i++) {
			System.out.println(arr2[i]);
		}
		System.out.println();
		
		//for each문을 활용 (arr2에 있는 값들이 하나씩 num에 대입)
		for (int num : arr2) {
			System.out.println(num);
		}
		System.out.println();
		
		
		
	}

}
