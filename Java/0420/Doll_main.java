package ex0420;

import java.util.ArrayList;
import java.util.Random;

public class Doll_main {

	public static void main(String[] args) {
		//랜덤으로 ~~~인형이 뽑힙니다 출력
		
		//1. ~~~ 인형이 뽑힙니다 출력될 수 있게 객체 생성
//		Ryan ryan = new Ryan();
//		Jjangu jjang = new Jjangu();
//		Ditto ditto = new Ditto();
//		
		//자바에서는 같은 타입만 묶이므로, Doll type으로 upcasting을하여 
		//같은 타입으로 만들어줌(Upcasting)이 필요한 이유!
		Doll ryan = new Ryan(); //Upcasting 하여 라이언을 선언
		Doll jjang = new Jjangu();
		Doll ditto = new Ditto();
		
//		ryan.pick();
//		jjang.pick();
//		ditto.pick();
		
		//랜덤
		Random r= new Random();
		
		//라이언 짱구 메타몽을 하나로 묶기!!
		//자바에서는 같은 타입만 묶임 > 모두 같은 Doll타입으로 묶어주기
		ArrayList<Doll> dollList = new ArrayList<Doll>();
		//각 객체들 ㅈ추가
		dollList.add(ryan);
		dollList.add(jjang);
		dollList.add(ditto);
		
		int random_num = r.nextInt(3);
		
		dollList.get(random_num).pick();
		dollList.get(random_num);//여기는 ryan이라는 객체가 담겨져 있음!
		
		
		//추상클래스 특징
		// 객체를 생성할 수 없음.
		//Doll d = new Doll();
		// 설계와 구현을 분리하기 위해 등장 개념.
		
		
		
		
		
	}

}
