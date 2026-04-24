package ex0422_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;



public class DAO {
	/// DAO : Data Access Object
	/// 정의 : DB에 있는 data에 접근하기 위해 사용하는 객체
	
	//전역변수로 선언해야 conn을 사용해서 close를 할 수 있음!
	Connection conn;
	PreparedStatement pst;
	ResultSet rs;
	//시작은 getconnection으로 시작해서 연결하고, 마지막에는 close로 connection을 닫아줘야함
	//connection,close 메소드들은 외부에서 접근할 수 없도록 private으로 만들고,
	//insert,delete 등의 메소드들을 호출해서 사용할 때만 접근할 수 있도록 구현.
	
	
	
	//db 연결 connection하기 위한 메소드
	private void getConnection() {
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			String url = "jdbc:oracle:thin:@localhost:1521:xe";
			String user = "hr";
			String password = "hr";
			
			conn = DriverManager.getConnection(url,user,password);
			
			if(conn!=null) {
				System.out.println("연결성공");
			}else {
				System.out.println("연결실패");
			}
			
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	// 사용한 객체를 닫아주는 메소드
	private void close() {
		try {
			if(conn!=null) {//conn객체가 존재할때만 닫아주기
				
				conn.close();
			}
			
			if(pst !=null) {
				pst.close();
			}
			
			if(rs !=null){
				rs.close();
			}
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	// insert 메소드
	// 매개변수를 받아서 원하는 값을 받도록 구현.
	public int insert(String userid, String pw, String name,int age) {
		getConnection(); 
		int cnt = 0;
		String sql = "insert into member values(?,?,?,?)";
		
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, userid);
			pst.setString(2, pw);
			pst.setString(3, name);
			pst.setInt(4, age);
			
			cnt = pst.executeUpdate();
			
			
			
			//return cnt; // try 문 안에서 선언하면 나오지 않음.
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		close();
		return cnt;
	}
	
	public int update(String pw,String userid) {
		getConnection();
		int cnt = 0;
		String sql = "update member set pw = ? where userid = ?";
		
		try {
			pst = conn.prepareStatement(sql);
			pst.setString(1, pw);
			pst.setString(2, userid);
			
			cnt = pst.executeUpdate();
		
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
		
		close();
		return cnt;
	}
	
	public int delete(String id) {
		getConnection();
		int cnt = 0 ;
		
		String sql = "delete from member where userid = ?";
		try {
			pst = conn.prepareStatement(sql);
			
			pst.setString(1, id);
			
			cnt = pst.executeUpdate();
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		close();
		return cnt;
	}
	
	public ArrayList<MemberVO> select() {
		getConnection();
		ArrayList<MemberVO> list = new ArrayList<MemberVO>();
		String sql = "select * from member";
		try {
			pst = conn.prepareStatement(sql);
			rs = pst.executeQuery();
			while(rs.next()) {
				String id = rs.getString("userid"); //아니면 순서대로 가져올거면 int를 넣어줘도 됨 
				String pw = rs.getString("pw");
				String name = rs.getString("name");
				int age = rs.getInt("age");
				
				//System.out.println(id+" : "+pw+" name: "+name+" age: "+age);
				//내가 읽어온 데이터를 저장해서 반환하도록 여기서 바로 출력하지 않도록 구현.
				
				
				MemberVO vo = new MemberVO(id,pw,name,age);
				
				list.add(vo);
				//더이상 불러올 수 있는 데이터가 없을때까지 반복해서 계속 ArrayList에 add를 통해 계속 받아 저장
			}
			
			
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		close();
		return list;
	}
	
	

}
