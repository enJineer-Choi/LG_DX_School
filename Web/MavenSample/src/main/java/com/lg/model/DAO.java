package com.lg.model;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import com.lg.database.SqlSessionManager;

// DAO(Data Access Object) : 실제로 쿼리를 실행시켜 DB에 접근하는 클래스
public class DAO {

	// 세션을 생성해줄 공장 가져오기
	SqlSessionFactory session = SqlSessionManager.getSqlSession();
	
	// 공장을 사용해서 세션을 생성 -> sql실행, commit, rollback 등의 역할 모두 수행
	SqlSession sqlSession = session.openSession(true); // true -> auto commit
	
	// 회원가입 기능 > 회원가입에 사용할 생성자 메소드
	public int join(VO vo) {
		
		// insert("실행시킬 쿼리의 경로", 쿼리실행시킬 때 넘겨줄 데이터)
		//com.lg.model.DAO 해당 쿼리문(MemberMapper.xml)에 존재하는 join id를 지닌 쿼리문 불러오기
		int cnt = sqlSession.insert("com.lg.model.DAO.join", vo);
		// cnt는 삽입한 레코드의 갯수를 담고있는 변수
		// cnt == 1이라면 회원가입 성공! 아니라면 실패..
		
//		if(cnt == 1) {
//			System.out.println("회원가입 성공!");
//		} 확인용 코드 
		
		sqlSession.close();
		return cnt;
		
		
	}

	
	//로그인 기능에 사용할 메소드
	public VO login(VO vo) { //현재 id,pw 만 전달받았음. > 하지만 수정사항을 하려면 nick도 필요
		//첫번째 null에 경로 작성, vo로 return값 전달
		vo = sqlSession.selectOne("com.lg.model.DAO.login", vo);
		
		
		sqlSession.close();
		return vo;
		
	}


	public int update(VO vo) {
		int cnt = sqlSession.update("com.lg.model.DAO.update", vo);
		sqlSession.close();
		return cnt;		
	}
	
	
	public int delete(String id) {
		int cnt = sqlSession.delete("com.lg.model.DAO.delete", id);
		sqlSession.close();
		return cnt;
		
	}
	
	
	
	
	
	
	
}
