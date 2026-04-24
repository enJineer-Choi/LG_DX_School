package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Ex02Insert {

	public static void main(String[] args) {
		//1. 동적로딩
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			
			String user = "hr";
			String password = "hr";
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			
			Connection conn = DriverManager.getConnection(url, user, password);
			
			if(conn != null) {
				System.out.println("connection success");
			}else {
				System.out.println("connection fail");
			}
			
			//3. SQL 문장이 통과할 수 있는 통로 (통로만 제작 -> SQL을 통과시키지 않음)
			String id = "csj";
			String pw = "12345";
			String name = "석진";
			int age = 21;
			
			//값들이 바뀔 수도 있고 재사용성을 용이하게 하기 위해 우선 변수로 선언
			
			//String sql = "insert into member values('test','123','test',20)";
			
			//바로 대입하지 않는 방법
			//1. 물음표로 변수자리를 비워서 선언
			String sql = "insert into member values(?,?,?,?)";
			
			
			//connection안에 있음! -> preparestatement가 통로이름임
			PreparedStatement psmt = conn.prepareStatement(sql);
			//2. 생성된 객체에 set method를 활용해, 어떤 번호에 어떤 변수를 대입할건지 선언
			psmt.setString(1, id);
			psmt.setString(2, pw);
			psmt.setString(3, name);
			psmt.setInt(4, age);
			// 업데이트 하기 전에 값들을 넣어줘야함!
			
			//4. SQL 실행 
			int row = psmt.executeUpdate();
			//int 반환이유 > 몇행이 실행되었는지 반환
			if(row > 0) {
				System.out.println("insert succes");
			}else {
				System.out.println("insert fail");
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
