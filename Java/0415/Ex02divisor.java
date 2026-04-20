package ex0415;

public class Ex02divisor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 2;i<=100;i++) {
			System.out.print(i+"의 약수 : ");
			for(int j=1;j<=i;j++) {
				
				if(i%j==0) {
					System.out.print(j+" ");
				}
			}
			System.out.println();
		}
	}

}
