package ex0415;

public class Ex11binarysearch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] array = { 1, 7, 16, 25, 30, 33, 41, 66, 78, 90 };
		int searchdata = 77;

		int low_index = 0;
		int high_index = array.length - 1;

		while (true) {
			// 처음 내가 짰던 코드

			int middle_index = (low_index + high_index) / 2;

			if (searchdata == array[middle_index]) {
				System.out.println(middle_index + "번째위치");
				break;
			} else if (searchdata > array[middle_index]) {
				low_index = middle_index + 1;
			} else if (searchdata < array[middle_index]) {
				high_index = middle_index - 1;
			}
//			System.out.println("찾는값이 없습니다");
			if (high_index - low_index < 1) {
				System.out.println("찾는 값이 없습니다!");
				break;
			}
			//1로 두면 마지막 부분을 계산하지 않을 가능성이 있음. 
			// low_index > high_index보다 커지면 정지로 작성하는게 로직상 더 깔끔하고 좋을듯

			// 이 코드는 반복 돌때마다 출력됨.
//			while (low_index <= high_index) {
//			int middle_index = (low_index + high_index) / 2;
//
//			if (searchdata == array[middle_index]) {
//				System.out.println(middle_index + "번째위치");
//				break;
//			} else if (searchdata > array[middle_index]) {
//				low_index = middle_index + 1;
//			} else if (searchdata < array[middle_index]) {
//				high_index = middle_index - 1;
//			}
//			System.out.println("찾는값이 없습니다");
//			}

		}
	}
}