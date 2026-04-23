package ex0422;

public interface Phone {
	//메소드 생성 (추상)
	void call();
	//default 메소드
	default void internet() {
		
	}
}
