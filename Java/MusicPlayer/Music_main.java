package MusicPlayer;

import java.util.Scanner;

public class Music_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		Musicplayercon player = new Musicplayercon();
		
		while(true) {
			System.out.print("[1]재생 [2]정지 [3]다음곡 [4]이전곡 [5]종료 >> ");
			int num = sc.nextInt();
			if(num==1) {
				//System.out.println(player.play());//이렇게 출력하면 주소값이 return
				Music m = player.play();
				int minute = m.getPlayTime()/60;
				int second = m.getPlayTime()%60;
				System.out.println(m.getMusicName()+", "+m.getSinger()+", "+minute+"분"+second+"초");
			}else if(num==2) {
				
				System.out.println(player.stop());
			}else if (num==3) {
				Music nplay = player.nextPlay();
				int minute = nplay.getPlayTime()/60;
				int second = nplay.getPlayTime()%60;
				System.out.println(nplay.getMusicName()+", "+nplay.getSinger()+", "+minute+"분"+second+"초");
			}else if (num==4) {
				Music pplay = player.prePlay();
				int minute = pplay.getPlayTime()/60;
				int second = pplay.getPlayTime()%60;
				System.out.println(pplay.getMusicName()+", "+pplay.getSinger()+", "+minute+"분"+second+"초");
			}else if (num==5) {
				System.out.println("프로그램 종료");
				break;
			}
		}
	}

}
