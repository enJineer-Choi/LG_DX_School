package ex0422;

public class Phone_class implements Phone ,Camera{
	//class가 interface 구현받는 키워드 - implements
	// 클래스에서도 interface를 여러개 작성가능!(interface에서만 가능한거 아님!)
	// interface를 상속받으면서 동시에 class도 상속이 가능
	
	@Override
	public void call() {
		System.out.println("전화 기능");
		
	}
	
	
}
