package ex0422_jdbc;

public class MemberVO {
	
	// Select를 통해 출력할 객체를 저장하기 위해 MemberVO 라는 클래스를 만들어서 데이터를 저장.
	private String id;
	private String pw;
	private String name;
	private int age;
	public MemberVO(String id, String pw, String name, int age) {
		super();
		this.id = id;
		this.pw = pw;
		this.name = name;
		this.age = age;
	}
	public String getId() {
		return id;
	}
	public String getPw() {
		return pw;
	}
	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	
	
}
