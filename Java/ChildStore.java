package ex0417;

public class ChildStore extends ParentsStore{

	public ChildStore(String name) {
		super(name);
		System.out.println("자식 생성자 실행");
	}

	@Override
	public void makeGalbi() {
		System.out.println("새로운 갈비 등장");
	}
	
	//기능추가
	public void makeRose() {
		System.out.println("로제 떡갈비 등장");
	}
	
	
}	
