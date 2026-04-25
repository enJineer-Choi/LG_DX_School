package com.ex01;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;


@WebServlet("/user-info")
public class Ex04UserInfo extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String job = request.getParameter("job");
		System.out.println(job);
		// 옵션의 value 값들이 출력이 됨.
		
		String gender = request.getParameter("gender");
		System.out.println(gender);
		
//		String hobby = request.getParameter("hobby");
//		System.out.println(hobby);
		//위처럼 작성하면 여러개를 선택했어도 가장 앞에 있는 값만 가져오게 됨. > 
		
		//여러개의 값을 받아오는 메소드(여러 값을 받아오고 싶을 때 String 배열로 return)
		String [] hobby = request.getParameterValues("hobby");	
		System.out.println(hobby);//주소값이 출력됨
		//for-each 문을 통해 각 배열의 값들을 출력해준다
		for(String s: hobby) {
			System.out.println(s);
		}
	}

}
