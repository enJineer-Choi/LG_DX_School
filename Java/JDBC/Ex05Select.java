package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Ex05Select {

	public static void main(String[] args) {
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
			
			String sql = "select * from member";
			PreparedStatement psmt = conn.prepareStatement(sql);
			
			//Insert,Delete,update는 실행문이 executeUpdate()를 활용
			ResultSet rs =  psmt.executeQuery();
			//rs -> DB에서 검색해온 값을 저장
			//rs.next() -> 다음 검색할 행이 있을시 true반환. 없을경우 false반환
			while(rs.next()) {
				String id = rs.getString("userid"); //아니면 순서대로 가져올거면 int를 넣어줘도 됨 
				String pw = rs.getString("pw");
				String name = rs.getString("name");
				int age = rs.getInt("age");
				
				System.out.println(id+" : "+pw+" name: "+name+" age: "+age);
			}
			
			
		} catch (Exception e) {//모든 상황을 예외처리 해줌.
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
