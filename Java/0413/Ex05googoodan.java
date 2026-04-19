package ex0413;

public class Ex05googoodan {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//2단 출력
		for (int i=1;i<10;i++){
			System.out.println("2*"+i+"="+2*i);
		}
		
		for (int j=2;j<10;j++) {
			for (int i=1;i<10;i++) {
				System.out.println(j+"*"+i+"="+j*i);
			}
			System.out.println();
		}
		
	}

}
