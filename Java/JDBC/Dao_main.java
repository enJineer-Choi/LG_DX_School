package ex0422_jdbc;

import java.util.ArrayList;
import java.util.Scanner;

public class Dao_main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		DAO dao = new DAO();
		ArrayList<MemberVO> li = dao.select();
		
	
		while(true) {
			System.out.print("1. 전체 회원조회 2. 회원가입 3. 회원정보 삭제 4. 비밀번호 수정 5. 회원검색 6. 종료 >> ");
			int num = sc.nextInt();
			if(num==1) {
				System.out.println("======전체 회원조회=======");
				if(li.size()==0) {
					System.out.println("등록된 정보가 없습니다.");
				}else {
					for(int i =0;i<li.size();i++) {
						System.out.printf("%d. %s(%d세)\t[ID/PW] %s / %s\n",i+1,li.get(i).getName(),li.get(i).getAge(),li.get(i).getId(),li.get(i).getPw());
					}
				}
			}
			else if(num ==2) {
				System.out.println("======회원가입======");
				System.out.print("ID : ");
				String id = sc.next();
				System.out.print("PW : ");
				String pw = sc.next();
				System.out.print("이름 : ");
				String name = sc.next();
				System.out.print("나이 : ");
				int age = sc.nextInt();
				System.out.println("회원가입 성공");
				
				
				int cnt = dao.insert(id, pw, name, age);
				if(cnt>0) {
					System.out.println("insert success");
				}else {
					System.out.println("insert fail");
				}
			}
			else if (num==3) {
				System.out.println("======회원정보 삭제========");
				System.out.print("삭제할 ID 입력 : ");
				String del_id = sc.next();
				int cnt = dao.delete(del_id);
				
				if(cnt >0) {
					System.out.println("삭제 성공");
				}else {
					System.out.println("삭제 실패");
				}
//				boolean t = true;
//				for (int i=0;i<li.size();i++) {
//					if(del_id.equals(li.get(i).getId())) {
//						li.remove(i);
//						t = false;
//						System.out.println("삭제 성공");
//					}
//				}
//				if(t==true) {
//					System.out.println("삭제 실패");
//				}
//				
//				
				
			}
			else if (num==4) {
				System.out.println("======비밀번호 변경========");
				System.out.println("ID 입력 : ");
				String id = sc.next();
				System.out.println("기존 비밀번호 입력 : ");
				String p_pw = sc.next();
				System.out.println("변경할 비밀번호 입력 : ");
				String f_pw = sc.next();
				
				for (int i =0;i<li.size();i++) {
					if(id.equals(li.get(i).getName())) {
						
					}
				}
				
				
			}
			else if (num==5) {
				
			}
			else if (num==6) {
				System.out.println("프로그램이 종료되었습니다.");
				break;
			}
		}

	}

}
