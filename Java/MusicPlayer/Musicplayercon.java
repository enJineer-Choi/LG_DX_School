package MusicPlayer;

import java.io.FileInputStream;
import java.util.ArrayList;

import javazoom.jl.player.Player;

public class Musicplayercon {
	//객체 생성시에 
	//ArrayList는 전역변수로 만들어줘야 다른 곳에서도 접근이 가능함.
	ArrayList<Music> musicList  = new ArrayList<Music>();
	
	int music_index = 0;
	
	Player player = null;
	public Musicplayercon() {
		//각 노래 객체를 생성하여 List에 추가. 
		musicList.add(new Music("뱅뱅뱅","빅뱅",100,"C://music//bangbangbang.mp3"));
		musicList.add(new Music("CheerUp","트와이스",120,"C://music//cheerup.mp3"));
		musicList.add(new Music("Daddy","싸이",200,"C://music//daddy.mp3"));
	}
	
	public void musicplay() {
		Thread t = new Thread(new Runnable() {
			
			@Override
			public void run() {
				try {
					FileInputStream fis = new FileInputStream(musicList.get(music_index).getmusicPath());
					player = new Player(fis);
					player.play();
					
					
				} catch (Exception e) {
					// TODO: handle exception
				}
				
				
			}
		});
		t.start();
		
	}
	
	public Music play() {
		musicplay();
		return musicList.get(music_index);
	}
	
	public Music nextPlay() {
		music_index++;
		
		
		if (music_index ==musicList.size()) {//인덱스가 사이즈랑 같으면이라고 해주면 됨
			music_index = 0;
		}
		stop();// 재생 중인 노래를 멈춤
		musicplay();
		return musicList.get(music_index);
		
		
		
	}
	public Music prePlay() {
		music_index--;
		if(music_index<0) {
			music_index = musicList.size()-1;
		}
		stop();
		musicplay();
		
		return musicList.get(music_index);
	}
	
	public String stop() {
		 if(player != null) {
			 player.close();
		 }
		 String result = "노래가 정지되었습니다";
		 return result;
	}
	
}
