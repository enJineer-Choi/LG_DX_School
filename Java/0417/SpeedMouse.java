package ex0417;

public class SpeedMouse extends Mouse{
	//왼쪽클릭이 다른 마우스보다 빠른 마우스
	//Method로 leftClick()과 rightClick()을 사용중임.
	//새로운 메소드를 만드는 것은 새로운 버튼을 만드는 것과 같아
	// leftClick()의 기능을 수정(재정의)
	// -> 메소드의 오버라이딩
	//메소드의 오버라이딩 조건
	//1. 메소드의 이름이 같아야함 -> 메소드의 오버로딩과 동일
	//2. 매개변수의 개수나 타입이 동일해야함
	//3. 리턴타입이 동일해야함
	//4. 접근제한자는 더 크거나 같아야함.
	//5. 상속관계여야함. 
	
	//오버라이딩 : 상속관계에서 기능을 재정의
	// 오버로딩 : 매개변수를 달리하여 기능을 추가
	
	//leftClick 오버라이딩
	// 만약에 오타가 났다면 -> 메소드 생성
	//오타나 오버라이딩 확인용으로 사용
	
	public void leftClick() {
		System.out.println("빠르게 좌측클릭");
	}


	//편하게 오버라이딩 하는법
	//alt + shift + s > Override / implements ~
	
	//@ -> annotation (컴파일러가 이해하는 코드)
	@Override
	public void rightClick() {
		// TODO Auto-generated method stub
		super.rightClick();
		//super > 부모 클래스에 있는 기능(메소드,변수 = 필드)을 호출하겠다는 의미
		System.out.println("안녕하세요~");
	}
	
}
