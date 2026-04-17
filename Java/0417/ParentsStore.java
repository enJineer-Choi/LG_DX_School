package ex0417;

public class ParentsStore {
	String name = "부모님 가게";
	
	//기본 생성자가 아닌 생성자를 만들 시 -> 자식클래스에서도 구현
	public ParentsStore(String name) {
		this.name = name;
		System.out.println("부모클래스 생성자 실행");
	}
	//떡갈비 만들기
	public void makeGalbi() {
		System.out.println("송정역 전통의 갈비를 만듭니다.");
	}
	
	//양념
	public void makeSauce() {
		System.out.println("송정역 전통의 양념 갈비를 만듭니다.");
	}
	
	//
	
}
