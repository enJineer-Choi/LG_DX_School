package ex0420;

public abstract class  Employee {
	// 사번, 이름, 연봉(일단)
	private String empNo;
	private String name;
	private int money;
	
	
	
	public Employee(String empNo, String name, int money) {
		this.empNo = empNo;
		this.name = name;
		this.money = money;
		
	}



	public String getEmpNo() {
		return empNo;
	}



	public String getName() {
		return name;
	}



	public int getMoney() {
		return money;
	}



	//추상 메소드로 getPay()
	//역할 : 계약직, 정규직, 아르바이트에 따라 급여계산 방법을 달리 할 수 있도록
	//서브클래스에서 오버라이딩 진행 (강제로)
	public abstract int getPay();
	
	
	
}
