package ex0420;

public class TempEmployee extends Employee{
	// 1. 부모클래스에 생성자가 있는 경우 자식클래스에도 있어야함.
	private int month;
	
	public TempEmployee(String empNo, String name, int money,int month) {
		super(empNo, name, money);
		this.month = month;
	}


	
	
	@Override
	public int getPay() {
		
		return getMoney()/month;//한달에 받는 금액을 알 수 있음
	}
	
}
