package ex0420;

public class Employee_main {

	public static void main(String[] args) {
		
		TempEmployee temp = new TempEmployee("E001","박원호",5000,6);
//		temp.empNo = "E001";
//		temp.name = "박원호";
//		temp.money = 5000;
//		temp.month = 6;
		//생성자를 만들어서 temp키워드가 먹히지 않음
		
		System.out.println("사번 : " + temp.getEmpNo());
		System.out.println("이름 : " + temp.getName()+"님의 급여는 ");
		System.out.println(temp.getPay()+"만원입니다");
		System.out.println();
		
		RegularEmployee regular = new RegularEmployee("E002","홍길동",3000,400,12);
		System.out.println("사번 : " + regular.getEmpNo());
		System.out.println("이름 : " + regular.getName()+"님의 급여는 ");
		System.out.println(regular.getPay()+"만원입니다");
		System.out.println();
		
		ParttimeEmployee prt1 = new ParttimeEmployee("E003", "이순신", 5, 10);
		System.out.println("사번 : " + prt1.getEmpNo());
		System.out.println("이름 : " + prt1.getName()+"님의 급여는 ");
		System.out.println(prt1.getPay()+"만원입니다");
		System.out.println();
		
		ParttimeEmployee prt2 = new ParttimeEmployee("E004", "임꺽정", 10, 20);
		System.out.println("사번 : " + prt2.getEmpNo());
		System.out.println("이름 : " + prt2.getName()+"님의 급여는 ");
		System.out.println(prt2.getPay()+"만원입니다");
	}

}
