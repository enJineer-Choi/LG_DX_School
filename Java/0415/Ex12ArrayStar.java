package ex0415;

public class Ex12ArrayStar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] starcount = {3,4,4,2,1};
		
		for (int num: starcount) {
			System.out.print(num + " : ");
			for (int i=1;i<=num;i++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

}
