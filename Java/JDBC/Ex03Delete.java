package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
public class Ex03Delete {
	public static void main(String[] args) {
		//1. 동적로딩
		try {
			///다른 DB 사용할 때는 밑에 부분만 변경해주면 됨.
			Class.forName("oracle.jdbc.driver.OracleDriver");
			
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			String user = "hr";
			String password = "hr";
			
			Connection conn = DriverManager.getConnection(url,user,password);
			
			if(conn!=null) {
				System.out.println("연결성공");
			}else {
				System.out.println("연결실패");
			}
			
			String sql = "delete from member where userid= ?";
			
			PreparedStatement psmt = conn.prepareStatement(sql);
			psmt.setString(1, "test");
			
			
			//4.SQL 실행
			
			int cnt = psmt.executeUpdate();
			if(cnt >0) {
				System.out.println("delete success");
			}else {
				System.out.println("delete fail");
			}
			
			
		} catch (Exception e) {//모든 상황을 예외처리 해줌.
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
