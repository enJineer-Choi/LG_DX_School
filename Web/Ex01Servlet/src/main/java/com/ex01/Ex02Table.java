package com.ex01;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/table")
public class Ex02Table extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		//string -> int로 변환
		//왜냐하면 HTML에서 테이블로 출력할 때 숫자형으로 출력하고 싶음
		// Integer.parseInt(문자열) > 숫자로변환
		
		
		String number = request.getParameter("number");
		
		int num = Integer.parseInt(number);
		//숫자형태인 문자열들 (ex "10")같은 것들은 변환 가능
		System.out.println(num+1900);		
		
		//2. 한글 인코딩하기
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();//출력도구를 만드는 코드
		//문자열로 HTML 태그 입력가능!
		out.print("<h1>"+num+"</h1>");
		
		out.print("<table border = 1>");
		out.print("<tr>");
		//반복을 돌며 td태그를 생성 (자바 코드이기 때문)
		for (int i =1;i<=num;i++) {
			out.print("<td>"+i+"</td>"); 
		}
		
		out.print("</tr>");
		out.print("</table>");
		
		
		
	}

}
