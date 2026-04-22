package MusicPlayer;

public class Mythread extends Thread{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		for (int i =0;i<10;i++) {
			System.out.println("Mythread : "+i);
			try {
				Thread.sleep(1000);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			// 강제성 생성. InterruptedException > 제한된 상황에서의 예외
			//Exception > 모든 예외상황
			//Thread.sleep(1000)은 try문 안에서 해야함 (예외상황 때문에_)
		}
	}
	
}
