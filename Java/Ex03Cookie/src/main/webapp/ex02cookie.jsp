<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<h1>쿠키 수정, 삭제 해보기</h1>
<%

//쿠키 생성
Cookie cookie = new Cookie("hello","world");

cookie.setMaxAge(60);
response.addCookie(cookie);

//쿠키 수정 코드 - setValue(수정값); --> addCookie()까지 진행해 주어야함
//cookie.setValue("내가만든쿠키");
//만들고 나서 add로 적용해주어야함.
//response.addCookie(cookie);

%>

<a href = "ex02cookie2.jsp">쿠키 삭제하기 </a>


</body>
</html>