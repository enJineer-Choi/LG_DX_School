package ex0422;

public interface Ex01Interface {
	// class에서 접근제한자 생략할 시 --> default
	// interface에서 접근제한자 생략할 시 -->public
	
	// 필드(변수) , 메소드로 구성
	// 필드는 상수만 가능 (final)
	// 기본적인 설정값이라고 생각하기(예시: 에러 코드, pi값 = 3.141592...)
	
	int num1 = 10;
	public static final int NUM2 = 20;// 원래의 풀네임
	//public static final은 생략 가능
	//상수이다 보니 값이 항상 할당되어야 함!
	//int NUM3; >에러남. 값이 할당되지 않아서
	//num1 = 20;
	
	
	//메소드 --> 추상메소드만 가능 (거짓)
		///jdk가 발전하면 일반 메소드 생성이 가능해짐
		/// 과거 버전에서는 안되는 경우가 있을 수 있음 (8버전)
	public abstract void test1();
	//public과 abstract 키워드는 생략이 가능
	void test2();
	//반환타입과 메소드이름만 존재
	
	//인터페이스 내 일반 메소드 생성 방법
	// 3가지 - default 메소드, static 메소드, private 메소드로 제작
	default void test3() {
		//인터페이스에서는 default를 명시해서 써줘야함.
		//추상메소드가 아님!!
		//강제성이 없음. > 오버라이딩 해주지 않아도 됨.
		//default자리에 다른 접근제한자만 바꾸면 됨.(static,private 모두 똑같음)
	}
}	
