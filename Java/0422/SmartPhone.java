package ex0422;

public interface SmartPhone extends Phone, Camera{
	///interface가 interface를 상속받는 키워드 -- extends
	// interface에서 class 상속은 불가능
	
	//Phone --> call()메소드를 SmarPhone에서 구현하는 것인 아니라
	//			SmartPhone을 구현하는 클래스에서 구현합니다!
	
	//interface는 구현을 하는 곳이 아님.
	
	//다중상속을 지원하고 있습니다!!
	
	
}
