package ex0420;

public class ParttimeEmployee extends Employee{
	private int day;
	
	public ParttimeEmployee(String empNo, String name, int money,int day) {
		super(empNo, name, money);
		this.day = day;
	}

	@Override
	public int getPay() {
		
		return day*getMoney();
	}

}
