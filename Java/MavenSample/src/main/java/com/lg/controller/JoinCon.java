package com.lg.controller;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

import com.lg.model.DAO;
import com.lg.model.VO;

@WebServlet("/JoinCon")
public class JoinCon extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		// 1. post방식 요청데이터 인코딩
		request.setCharacterEncoding("UTF-8");
		
		// 2. 요청데이터 가져오기
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String nick = request.getParameter("nick");
		
		// 3. 데이터 잘 넘어오는지 확인하기
		System.out.println(id + pw + nick);
		
		// id, pw, nick 하나의 객체(데이터타입)로 묶어주기
		VO vo = new VO(id, pw, nick);
		
		int cnt = new DAO().join(vo);
		
		//cnt가 1 이라면 회원가입 성공이므로 Main.jsp로 이동
		if(cnt ==1) {
			//쿼리스트링 기법 : url 뒤에 데이터를 담아서 전송
			//url?key=value&key=value (여러개를 보내고 싶을 때는 &로 연결해서 보내면 됨) > 객체나 문자열을 담을 수 없음
			
			//response.sendRedirect("Main.jsp?result=success");
			// sendRedirect는 request,response 방식을 2번씩 사용.
			
			
			//forwarding 방식 페이지 이동
			// request,response 객체를 한번씩만 사용. 
			RequestDispatcher rd = request.getRequestDispatcher("Main.jsp");
			request.setAttribute("result","success");
			rd.forward(request, response);
			
		}
		else {
			//아니라면, Join.jsp로 이동하도록 
			response.sendRedirect("Join.jsp");
			
		}
	
	
	}

}
