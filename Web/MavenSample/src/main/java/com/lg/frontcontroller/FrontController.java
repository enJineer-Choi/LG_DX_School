package com.lg.frontcontroller;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

import com.lg.controller.Command;
import com.lg.controller.DeleteCon;
import com.lg.controller.JoinCon;
import com.lg.controller.LoginCon;
import com.lg.controller.LogoutCon;
import com.lg.controller.UpdateCon;
import com.lg.model.DAO;
import com.lg.model.VO;

@WebServlet("*.do")
public class FrontController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// frontcontroller는 모든 요청을 받는 servlet
		// * : 전체 파일을 뜻함
		// .do : .do 확장자 의미
		// *.do : .do 확장자가 붙으면 전부 여기로 모음
		// DeleteCon,JoinCon,LoginCon,Logoutcon,UpdateCon를 모두
		System.out.println("[FrontController]");

		// 어디서 요청이 들어왔는지 확인!!
		// 문자열 형태로 어디서 요청이 들어왔는지 알려줌
		String requestURI = request.getRequestURI();

		// 요청이 들어온 주소
		System.out.println("요청 주소 : " + requestURI);
		/// MavenSample/~~.do

		// context path 가져오기
		String contextpath = request.getContextPath();
		System.out.println(contextpath);
		/// MavenSample

		// 어차피 Contextpath는 모두 다 똑같으므로, .do부분만 작성하고 싶음.
		// 문자열 자르는 메소드 사용.
		/// substring(beginindex) : 처음부터 beginindex까지 잘라내기
		/// substring(beginindex,endindex) : beginindex부터 endindex까지 잘라내기 :endindex는
		// 포함되지 않음
		String result = requestURI.substring(contextpath.length() + 1);
		System.out.println("요청 실제 Servlet : " + result);

		// 1. post방식 요청데이터 인코딩 > 동일하게 사용되므로 조건문 밖에서 실행
		request.setCharacterEncoding("UTF-8");

		Command con = null;

		if (result.equals("JoinCon.do")) {
			con = new JoinCon();
			// command의 JoinCon을 업캐스팅해서 저장
		}

		else if (result.equals("LoginCon.do")) {
			con = new LoginCon();
		}

		else if (result.equals("LogoutCon.do")) {
			con = new LogoutCon();
		} 
		else if (result.equals("UpdateCon.do")) {
			con = new UpdateCon();

		}
		else if (result.equals("DeleteCon.do")) {
			con = new DeleteCon();

		}
		
		
		String moveURL = con.execute(request, response);
		// forward:Main.jsp , redirect:Join.jsp

		if (moveURL.startsWith("forward:")) {
			RequestDispatcher rd = request.getRequestDispatcher(moveURL.substring(8));
			rd.forward(request, response);
		} else if (moveURL.startsWith("redirect:")) {
			response.sendRedirect(moveURL.substring(9));
		}
	}

}
