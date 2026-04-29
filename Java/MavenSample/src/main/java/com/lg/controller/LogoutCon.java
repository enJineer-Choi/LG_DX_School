package com.lg.controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

//1. 로그아웃 버튼을 눌렀을때 Logoutcon이라는 servlet으로 이동
//2. 로그인했을때 세션에 저장한 값을 지우기
//3. Main.jsp 페이지로 이동


@WebServlet("/LogoutCon")
public class LogoutCon extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();
		
		//2가지 방법
		//1. 내가 했던 방법
		session.invalidate();
		//2.session.removeAttribute("nick");
		
		//3. Main.jsp로 페이지 이동
		response.sendRedirect("Main.jsp");
	}

}
