package com.lg.controller;

import com.lg.model.DAO;
import com.lg.model.VO;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class UpdateCon implements Command{

	@Override
	public String execute(HttpServletRequest request, HttpServletResponse response) {


		
		String id = request.getParameter("id"); // 수정불가능한 고유한 값
		String pw = request.getParameter("pw");
		String nick = request.getParameter("nick");
		
		VO vo = new VO(id,pw,nick);
		int cnt = new DAO().update(vo);
		
		if(cnt == 1) {
			//회원 수정 성공
			HttpSession session =  request.getSession();
			session.setAttribute("vo", vo);
			//vo 객체로 이름을 저장해야 
			//response.sendRedirect("Main.jsp");
			
			return "redirect:Main.jsp";
					
			
		}else {
			//회원 수정 실패
			//response.sendRedirect("Update.jsp");
			return "redirect:Update.jsp";
		}
	
	
	}

}
