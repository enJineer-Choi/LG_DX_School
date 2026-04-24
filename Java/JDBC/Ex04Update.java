package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class Ex04Update {

	public static void main(String[] args) {
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			
			String user = "hr";
			String password = "hr";
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			
			Connection conn = DriverManager.getConnection(url,user,password);
			
			if(conn!=null) {
				System.out.println("연결성공");
			}else {
				System.out.println("연결실패");
			}
			
			String sql = "update member set pw = ? where userid = ?";
			
			PreparedStatement psmt =  conn.prepareStatement(sql);
			psmt.setString(1, "0000");
			psmt.setString(2, "csj");
			
			int cnt = psmt.executeUpdate();
			
			
			
			
			if(cnt>0) {
				System.out.println("update success");
			}else {
				System.out.println("update fail");
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
