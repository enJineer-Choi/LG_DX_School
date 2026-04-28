package ex01.shop;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

import java.net.URLEncoder;


@WebServlet("/Shop")
public class Ex03Shop extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//checkbox로 되어있을때는 name = "product의 값으로 가져와서 value로 
		
		//데이터 가지고오기
		String[] products = request.getParameterValues("product");
		
		//쿠키를 사용하여 데이터 저장
		for (int i = 0 ;i<products.length;i++) {
			
			//인코딩 진행
			String data = URLEncoder.encode(products[i],"UTF-8");
			
			Cookie cookie = new Cookie("items"+i,data);
			
			//문제점 발생 --> name값 중복 허용 X -> 마지막 값만 itmes라는 name으로 저장
			//두번째 문제 --> 띄어쓰기 존재하기 때문에 인코딩 필요 -> 출력시 디코딩 필요
			
			cookie.setMaxAge(180);
			
			response.addCookie(cookie);
		}
		
		// view로 돌아가기(jsp로 돌아가야함 --> client한테 다시 xxxx페이지로 이동해줘 라고 지시)
		response.sendRedirect("ex03shop.jsp");
		
		
		
		
	}

}
