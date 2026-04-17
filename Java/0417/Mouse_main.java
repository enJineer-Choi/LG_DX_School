package ex0417;

public class Mouse_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Mouse mouse = new Mouse();
		//ctrl 누른 상태에서 마우스로 메소드 어떻게 만들어졌는지 확인가능
		
		//메소드에서 다시 main으로 돌아가고 싶으면 alt+왼쪽 방향키
		
		mouse.leftClick();
		mouse.rightClick();
		System.out.println("==============");
		
		WheelMouse wm = new WheelMouse();
		wm.leftClick();
		wm.rightClick();
		System.out.println("================");
		
		SpeedMouse sm = new SpeedMouse();
		sm.leftClick();
		sm.rightClick();
	}

}
