package ex0408;

public class Ex02operator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num1 = 10;
		float num2 = 7.0f;
		System.out.println(num1/num2);
		//문자열 연산
		String s1 = "hello";
		String s2 = "world";
		
		System.out.println(s1 + s2);
		
		//문자열 + 정수형
		System.out.println(s1+num1);
		//hello num1 과 num2 더해진
		//hello17를 출력하고 싶음 >괄호를 하면 됨
		System.out.println(s1 + (num1+num2));
		
		System.out.println(s1 + num1+num2);
		//괄호를 씌우지 않으면 hello107.0
		//문자랑 정수랑 더해지면 더 큰 문자형으로 바뀜
		
	}

}
