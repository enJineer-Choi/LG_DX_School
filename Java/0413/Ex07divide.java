package ex0413;

public class Ex07divide {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//약수 ? -> 나누어 떨어지는 수
		//32의 약수
		System.out.print("32의 약수 :");
		for(int i=1;i<=32;i++) {
			if(32%i==0) {
				System.out.print(i+" ");
			}
		}
		
		//심화 -> 알고리즘 시간을 절반으로 단축
		//약수는 1을 제외하고 가장작은 정수는 2
		//32/2까지만 해도 됨. 16~32중간에는 32의 약수가 존재할 수가 ㅇ벗음.
		//근데 32가 포함이 안되므로 나중에 추가해주면 됨.
		System.out.print("32의 약수 :");
		for(int i=1;i<=32/2;i++) {
			if(32%i==0) {
				System.out.print(i+" ");
			}
		}
		System.out.print(32);
	}	

}
