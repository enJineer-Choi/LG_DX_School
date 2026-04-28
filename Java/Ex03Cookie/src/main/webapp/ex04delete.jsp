<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>세션 삭제 페이지</h1>
<%
	//session 삭제 메소드 -> .removeAttribute(name값)
	session.removeAttribute("test");
	
	String s = (String) session.getAttribute("test");	
	
	session.removeAttribute("age");
	
	//int는 클래스가 아니기 때문에 Object -> Integer -> int
	//test의 값을 지우고 나니 -> null로 반환
	//기본타입은 null을 지니고 있지 않음.
	//따라서 여기서는 Integer로 만들어주어야함
	
	Integer age = (Integer) session.getAttribute("age");
	
	// 한번에 모든 세션 삭제하는 방법
	session.invalidate();
	
%>
세션값 확인 하기 : <%= s %> <br>
int 세션값 확인하기 : <%= age %>

 -->
</body>
</html>