package com.lg.controller;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class LogoutCon implements Command{
	


	@Override
	public String execute(HttpServletRequest request, HttpServletResponse response) {
		HttpSession session = request.getSession();
		
		//2가지 방법
		//1. 내가 했던 방법
		session.invalidate();
		//2.session.removeAttribute("nick");
		
		//3. Main.jsp로 페이지 이동

		return "redirect:Main.jsp";
	}
}