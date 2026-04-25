package com.ex01;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;


@WebServlet("/login")
public class Ex03Login extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	//get,post 방식과는 상관이 없이 클라이언트 요청 처리
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String userId = request.getParameter("userId");
		String password = request.getParameter("password");
		
		System.out.println(userId+" "+password);
		//2. 한글 인코딩하기
		response.setContentType("text/html;charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		out.print(userId+ "님 환영합니다.");
		
	}

}
