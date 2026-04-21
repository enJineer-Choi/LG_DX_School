package ex0420;

public abstract class Doll {
	//Doll의 역할은 상속용임.
	
	//추상클래스
	// 생김새 : class앞에 abstract 키워드가 붙은 클래스
	// abstract 키워드가 붙는 조건
		// 1. 1개이상의 추상메소드를 가지고 잇는 경우
		// 2. 단순히 class 앞에 abstract 키워드를 작성한 경우
	// 추상 메소드는 반드시 추상클래스 안에 존재해야한다 O
	// 추상클래스는 반드시 추상메소드를 가져야한다 X > 
		//추상클래스는 메소드 없이도 그냥 선언할 수 있음

	
	//추상클래스는 추상메소드가 아닌 다른 메소드도 사용 가능!
	//일반메소드 > overiding해야하는 강제성이 없음
	public void print() {
		
	}
	public abstract void pick();
	//추상메소드
	// 생김새 : body()가 없고, abstract 키워드가 붙은 메소드 
	// 기능 : 서브 클래스에서 반드시 구현(오버라이딩)해야하는 메소드 (강제성)
	// 
	
	
	//public void pick();
		//이 메소드 역시 override를 하기 위한 용도임
		//그래서 body를 삭제하고 위처럼 abstract로 만듬
}

