package ex0420;

public class RegularEmployee extends Employee{
	private int bonus;
	private int month;
	
	public RegularEmployee(String empNo, String name, int money,int bonus,int month) {
		super(empNo, name, money);
		this.bonus = bonus;
		this.month = month;
		// TODO Auto-generated constructor stub
	}

	@Override
	public int getPay() {
		
		return (getMoney()+bonus)/month;
	}
	
}
