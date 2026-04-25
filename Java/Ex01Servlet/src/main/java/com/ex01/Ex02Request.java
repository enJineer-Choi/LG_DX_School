package com.ex01;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;


@WebServlet("/req")
public class Ex02Request extends HttpServlet {
	private static final long serialVersionUID = 1L;
    
	//클라이언트가 보내주는 값을 처리하는 메소드
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    	
    	//form 태그에 전송방식을 작성하지 않았을때 GET방식
    	
    	//데이터 받아주기
    	
    	//요청한 데이터를 꺼내오기! --> input 태그의 name 값 입력!
    	String data = request.getParameter("data");
    	//request.getParameter() return값은 무조건 String
    	// 즉, 입력한 모든 값은 String으로 
    	
    	System.out.println(data);
    	
    	///저장 > 웹페이지 새로고침 > 동기화 > html파일 실행
    	
    	//응답진행 
    	//직접 그리기 
    	//2. 한글 인코딩하기
    	response.setContentType("text/html;charset=UTF-8");
    	//3. 출력 도구 만들기
    	PrintWriter out = response.getWriter();//클라이언트한테 다시 보여줄 화면을 만드는 작업
    	//4. 웹 화면에 출력하기 
    	out.print("내가 입력한 값은 : " + data);
    	
    	//null 값이 나올 경우 > 
    	//servlet은 백엔드 부분이라 HTML에서 값을 받아오지 않기 때문에 servlet만 실행시키면 null값이 나올수밖에 없음
    	
    	
    	
    	
    }

}
