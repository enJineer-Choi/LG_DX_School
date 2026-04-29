package com.lg.frontcontroller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;


@WebServlet("*.do")
public class FrontController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//frontcontroller는 모든 요청을 받는 servlet
		// * : 전체 파일을 뜻함
		//.do : .do 확장자 의미
		//*.do : .do 확장자가 붙으면 전부 여기로 모음
		//DeleteCon,JoinCon,LoginCon,Logoutcon,UpdateCon를 모두 
		System.out.println("[FrontController]");
		
		//어디서 요청이 들어왔는지 확인!!
		//문자열 형태로 어디서 요청이 들어왔는지 알려줌
		String requestURI = request.getRequestURI();
		
		//요청이 들어온 주소
		System.out.println("요청 주소 : " + requestURI); 
		///MavenSample/~~.do
		
		//context path 가져오기
		String contextpath = request.getContextPath();
		System.out.println(contextpath);
		///MavenSample
		
		//어차피 Contextpath는 모두 다 똑같으므로, .do부분만 작성하고 싶음.
		//문자열 자르는 메소드 사용.
		///substring(beginindex) : 처음부터 beginindex까지 잘라내기
		/// substring(beginindex,endindex) : beginindex부터 endindex까지 잘라내기 :endindex는 포함되지 않음
		String result = requestURI.substring(contextpath.length()+1);
		System.out.println("요청 실제 Servlet : " + result);	
		
		if(result.equals("JoinCon.do")) {
			System.out.println("회원가입기능");
		}else if(result.equals("LoginCon.do")){
			System.out.println("로그인 기능");
		}else if(result.equals("LogoutCon.do")){
			System.out.println("로그아웃 기능");
		}else if(result.equals("UpdateCon.do")){
			System.out.println("회원수정 기능");
		}else if(result.equals("DeleteCon.do")){
			System.out.println("회원탈퇴 기능");
		}
		
	}

}
