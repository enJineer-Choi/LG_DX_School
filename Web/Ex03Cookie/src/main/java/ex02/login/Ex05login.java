package ex02.login;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

//2. 넘어온 id,pw값을 받은 후, id값을 main으로 전달하여 출력
@WebServlet("/loginCheck")
public class Ex05login extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//세션 객체 생성
		HttpSession session = request.getSession();
		
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		
		if(id.equals("test") && pw.equals("1234")) {
			//로그인 성공
			//세션에 값 추가
			//session.getAttribute(); // 불가능
			//jsp에서는 session이 내장객체였기 때문에 가능했음
			//하지만 servlet은 내장객체가 request와 response밖에 없음. 그래서 생성해 줘야함
			session.setAttribute("id", id);
			
			
			//ex05main.jsp로 이동
			response.sendRedirect("ex05main.jsp");
			
			
		}
	}

}
