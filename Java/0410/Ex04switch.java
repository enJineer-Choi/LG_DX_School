package ex0410;

public class Ex04switch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//switch문
		//기본문법
		//switch(식){
		//	case 값: 
		//}
		int num1 = 10;
		switch (num1) {// 소괄호에 작성된 식과 case에 작성된 value와 비교한 후, 일치하게 되면 실행
		case 65+55://연산도 가능
			System.out.println("65입니다");
			break;
		case 19:
			System.out.println("10입니다"); //일치하는 case를 만났을때 출력
			break;
		default:
			System.out.println("값이 없습니다");
			break;
		}
	}

}
