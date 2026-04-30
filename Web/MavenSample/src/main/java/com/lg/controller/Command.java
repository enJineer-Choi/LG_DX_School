package com.lg.controller;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

public interface Command {
	
	//interface -> body 부분이 없는 추상메소드만 존재
	//			-> interface를 상속받는 클래스는 인터페이스에 정의된 메소드를 무조건 구현해야함
	public String execute(HttpServletRequest request, HttpServletResponse response);
	
}
