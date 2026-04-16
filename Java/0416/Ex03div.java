package ex0416;

public class Ex03div {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num1 = 9;
		int num2 = 2;
		boolean divisor = isDivisor(num1,num2);
		System.out.println(divisor);
		
		getDivisor(10);
		System.out.println();
		getDivisor(24);
		System.out.println();
		getDivisor(100);
		
	}
	
	public static boolean isDivisor (int num1, int num2) {
		if(num1%num2 == 0) {
			return true;
		}else {
			return false;
		}
		//boolean return값을 가져야할 때는 false까지 있어야 완성!
		//타입을 선정할 땐 "boolean" 소문자로 적어주는게 좋음!
		
	}
	
	public static void getDivisor(int num) {
		System.out.print(num+"의 약수 : ");
		for(int i = 1 ;i<=num;i++) {
			if(num%i ==0) {
				System.out.print(i+" ");
			}
		}
	}

}
