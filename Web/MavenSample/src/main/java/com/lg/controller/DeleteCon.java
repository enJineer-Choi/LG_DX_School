package com.lg.controller;

import com.lg.model.DAO;
import com.lg.model.VO;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class DeleteCon implements Command{

	@Override
	public String execute(HttpServletRequest request, HttpServletResponse response) {


		// View에서 회원탈퇴 버튼을 누름 -> Controller도 아무정보가 없음 ->DAO에 있는 delete(id) 메소드에게 뭔가를
		// 넘겨줘야함
		// 현재 로그인한 사람만 삭제버튼을 누를 수 잇음 > 그래서 session에 저장된 id값을 넘겨주면 삭제 가능
		HttpSession session = request.getSession();
		VO vo = (VO) session.getAttribute("vo"); // id,pw,nick이 모두 존재
		String id = vo.getId();

		int cnt = new DAO().delete(id);
		// DAO에 delete()를 만들어서 만약 회원 탈퇴가 성공했다면

		// session 값 삭제 후 Main.jsp로 이동
		if (cnt == 1) {
			session.invalidate();
		}
		//response.sendRedirect("Main.jsp");

		// 삭제를 성공하든 실패하든 일단 Main.jsp로 이동하도록

	
		return "redirect:Main.jsp";
	}

}
