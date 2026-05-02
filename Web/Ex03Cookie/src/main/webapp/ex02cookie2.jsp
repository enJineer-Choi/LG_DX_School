<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>쿠키 삭제 페이지</h1>

<%
	//쿠키를 삭제하는 메소드는 없지만 없애는 법이 존재
	//시간을 0 으로 초기화 시키면 됨. --> 기존에 존재하고 있는 cookie의 name값의 maxAge를 0으로 수정
	
	//쿠키의 name값은 중복이 안됨.
	//같은 name의 쿠키를 생성하게 되면, 기존 쿠키가 사라지고 새로운 쿠키가 생성됨
	
	Cookie cookie = new Cookie("hello","");
	//처음에 안됐던 이유 : 이름이 동일하지 않아서!
	cookie.setMaxAge(0);
	response.addCookie(cookie);



%>


</body>
</html>