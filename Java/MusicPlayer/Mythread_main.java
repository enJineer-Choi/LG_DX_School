package MusicPlayer;

public class Mythread_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Mythread t = new Mythread();
		t.start(); //실행시키고 싶으면 run이 아니라 start
		
		//Runnable은 객체를 생성해서 사용하지 않음
		Thread t2 = new Thread(new MyRunnable());
		t2.start();

		//가장 많이 사용하는 방법 Runnableㅈ
		Thread t3 = new Thread(new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				try {
					for(int i =60;i<70;i++) {
						System.out.println("Real_Main : "+i);
						Thread.sleep(1000);
					}
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
		t3.start();
		try {
			for (int i =20;i<30;i++) {
				System.out.println("Main : "+i);
				Thread.sleep(1000);
			}
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		
	}

}
