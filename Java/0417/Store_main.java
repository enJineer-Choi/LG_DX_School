package ex0417;

public class Store_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 업캐스팅 > 자식클래스가 부모클래스로 되는 것
		// 부모 클래스 변수명 = new 자식클래스

		//생성자가 있는 경우 부모 - 자식 순으로 생성
		ParentsStore ps = new ChildStore("안녕");

		// 업캐스팅의 본체는 자식 (new 된 대상자를 봐야함 즉, ChildStore())
		ps.makeGalbi(); // 새로운 떡갈비라고 출력
		// --> 오버라이딩 된 경우 오버라이딩된 메소드를 실행
		ps.makeSauce();
		// ps.makeRose() 안됨 -> 부모클래스의 변수와 메소드에만 접근이 가능!!

		System.out.println(ps.name);// 부모님가게로 출력
		// 본체는 자식클래스이지만, 상속받은 건 부모의 필드값과 메소드를 상속받았으므로
		
		
		//다운캐스팅 > 강제 형변화
		//(업캐스팅 된 자식클래스만) 부모클래스가 (다시)-> 자식클래스
//		ChildStore cs = (ChildStore) new ParentsStore("hello");
//		cs.makeGalbi();
//		cs.makeRose();
//		cs.makeSauce();
		//실행하면 에러남. 
		// 다운캐스팅은 부모클래스로 업캐스팅된 자식클래스가 다시 자식클래스로 내려오는느낌?
		ChildStore cs = new ChildStore("hello");
		cs = (ChildStore) ps;
		// 부모클래스로 올라갔던 자식클래스를 다운캐스팅
		cs.makeRose();
	}

}
