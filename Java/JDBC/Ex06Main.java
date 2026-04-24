package ex0422_jdbc;

import java.util.ArrayList;

public class Ex06Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DAO dao = new DAO();
//		int cnt = dao.insert("ABC", "123957", "짱구", 30);
//				
//		int cnt = dao.update("13412345", "ABC");
		
//		int cnt = dao.delete("ming");
//		if(cnt >0) {
//			System.out.println("성공");
//		}else {
//			System.out.println("실패");
//		}
		ArrayList<MemberVO> li = dao.select();
		if(li.size()==0) {
			System.out.println("데이터가 없습니다");
		}else {
			for(int i =0;i<li.size();i++) {
				System.out.println(li.get(i).getName());
			}
		}
		
	}

}
