package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Ex01Connection {

	public static void main(String[] args) {
		//jar (자바 아카이브) > interface, class가 집결되어있는 확장자
		//ojdbc jar파일 삽입 
		
		//동적 로딩 -> 어떤 데이터베이스와 연결할 것인지를 작성해주는 코드
		//현재에러발생 
		//에러 이유 
		// 런타임에러 : 실행해야나는 에러지만, 치명적인 런타임에러는 오류 표시 
		//(오타 및 파일이 없는 경우를 방지하기 위해 미리 에러 표시)
		//> 해결방법 : Surround and try catch  
		//try - catch : 예외처리 구분
		//일단 실행 (try) ->오류나면 (catch)문을 실행
		try {
			//어떤 DB쓸건지만 명시한 과정.
			Class.forName("oracle.jdbc.driver.OracleDriver");
			
			//연결
			//연결을 위해 DB 계정 user,password 입력
			String user = "hr";
			String password = "hr";
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			//jdbc:oracle:thin --> java에서 oracle db 연결하는 방식
			//localhost --> IP 주소(지금 사용중인 컴퓨터)/ 그냥 주소도 가능
			//1521 --> oracle이 사용하는 포트번호
			//xe --> 오라클 db 버전 이름
			
			//이것도 여전히 에러 발생하므로 (3번째 catch문을 작성하여 예외처리를 작성해줌)
			Connection conn = DriverManager.getConnection(url, user, password);
			//connection안에 있는 추상메소드 기능이 부여됨
			if(conn!=null) {
				System.out.println("연결 성공!");
			}else {
				System.out.println("연결 실패!");
			}
			
			
			
			
			
			
			
			
			
			
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}

}
