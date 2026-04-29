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


@WebServlet("/LoginCon")
public class LoginCon extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		//요청데이터 post방식 인코딩
		request.setCharacterEncoding("UTF-8");
		//요청데이터 가져오기
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		//콘솔창에 데이터 잘 넘어오는지 확인
		System.out.println(id+pw);
		
		VO vo = new VO(id, pw);
		
		
		vo = new DAO().login(vo);
		
		if(vo != null) {
			//로그인 성공
			//서블릿에서는 session이 내장 객체가 아니기 때문에 생성해야함
			HttpSession session = request.getSession();
			session.setAttribute("vo", vo);
					
			
		}
		response.sendRedirect("Main.jsp");
		
	}

}
