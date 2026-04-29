package com.lg.controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

import com.lg.model.DAO;
import com.lg.model.VO;

@WebServlet("/UpdateCon")
public class UpdateCon extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
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
			response.sendRedirect("Main.jsp");
			
		}else {
			//회원 수정 실패
			response.sendRedirect("Update.jsp");
		}
	}

}
