package ex0422;

public class Phone_main {

	public static void main(String[] args) {
		//인터페이스 객체 생성 할 수 없음.
		// 안되는 이유 : 추상 메소드때문임. 
		//(추상 메소드 자체에 기능이 구현이 안되어있는데 구현자체가 안됨)
		// 그럼에도 만약에 new {오버라이딩 진행 한다면} 객체 생성 가능 -> 하지만 이렇게 잘 작성하지 않음
		
		Phone phone = new Phone() {

			@Override
			public void call() {
				// TODO Auto-generated method stub
				
			}
			
		};
		
	}

}
