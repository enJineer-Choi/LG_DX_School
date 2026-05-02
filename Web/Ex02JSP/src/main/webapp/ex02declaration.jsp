<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%--3.선언문 (declaration)
- JSP 내에서 변수나 메소드를 "전역변수"로 구성하는 요소
- 위치에 상관없이 가장 상단에 있다

* 4가지 구성요소들 중 가장 사용빈도 낮음
<%!  %>

 --%>
<%= num1 %>
<!-- 느낌표 지우면 순서에 맞지 않게 선언되어서 에러남-->
<%! int num1 = 10; %>



</body>
</html>