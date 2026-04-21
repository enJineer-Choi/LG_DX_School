package ex0420;

public class Ex01Access_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Ex01Access acc = new Ex01Access();
		System.out.println(acc.pub);
		// public : 같은 프로젝트 내에서는 어디서든지 사용가능(패키지가 분리되어 있어도)
		// 프로젝트 ? 여기서는 Ex01을 의미 
		
		
		//protected / default는 같은 패키지 안에서만 사용가능
		System.out.println(acc.pro);
		// 
		
		System.out.println(acc.def);
		//
		
		//System.out.println(acc.pri); 
		//private는 생성한 클래스 자체만 접근가능
	}	

}
