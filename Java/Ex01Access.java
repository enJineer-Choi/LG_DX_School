package ex0420;

// 접근 제한자
public class Ex01Access {
	//access modifier
	//자바에서는 4개의 접근제한자를 가지고 있음
	// public, protected, default, private
	
	//접근제한자 활용하여 변수 만들고 해당 변수 접근 범위 확인 
	
	public String pub = "public";
	protected String pro = "protected";
	String def = "default"; 
	// class에서 default는 생략. (명시해서 작성하지 않음)
	
	//그동안 작성해왔던 코드들 int num = 5; (모두 접근제한자가 없었던게 아니라 default임)
	private String pri = "private";
	
	
}
