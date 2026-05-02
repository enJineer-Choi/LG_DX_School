package com.ex01;

import jakarta.servlet.ServletConfig;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

/// Annotation이란?
/// - 클래스나 필드, 메소드에 부가정보를 등록하는 기능
/// - 컴파일 배포나 실행시 참조할 수 있는 주석


@WebServlet("/test")
public class Ex01Test extends HttpServlet {
	//객체를 byte 코드로 직렬화 하는 코드 
	//해당코드는 현재 파일이 Servlet임을 알려주는 아이디값.
	//0,1 ->작성한 코드를 byte 코드로 변환.
	//클래스 파일은 복잡하다보니, 객체 배열로 변환 후 진행 --> 직렬화
	private static final long serialVersionUID = 1L;

    
	//Method
	
    public Ex01Test() {
    	//객체가 생성되었을때 실행하는 코드
    	System.out.println("생성자 실행");
    }

    ///init : initialize 
    /// 초기값을 설정하는 메소드 (서버 실행 시 딱 한번만 실행되는 코드)
    /// 
	public void init(ServletConfig config) throws ServletException {
		//throws --> 예외처리 키워드 (try-catch보다 넓은 범위)
		//try-catch는 내가 원하는 만큼만 예외처리하는 방법 
		//throws : 메소드의 모든 코드를 예외처리하는 방법
		System.out.println("init 메소드 호출");
	}

	
	// server가 종료되었을때(실행시키고 있는 Tomcat 서버가 Stopped) 실행되는 메소드
	public void destroy() {
		System.out.println("destory 메소드 호출");
	}
	
	/// service의 역할 : Client의 요청을 처리하는 역할
	/// 요청방식이 어떠한 방식이든 처리하는 메소드 (get,post,put,fetch)
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		/// Request와 Response 진행....
		System.out.println("Service 호출");
	}

}
