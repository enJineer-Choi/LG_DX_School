package ex0415;

public class Ex01googoo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 2; i <= 9; i++) {
			System.out.print(i + "단 : ");
			for (int j = 1; j <= 9; j++) {
				System.out.print(i + " * " + j + " = " + j * i + " ");

			}
			System.out.println();
		}
	}

}
//반복문이 어려울 때는 일단 일일이 작성을 해보고, 그 안에서 규칙을 찾아 완성
