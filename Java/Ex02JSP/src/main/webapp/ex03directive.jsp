<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page errorPage = "ex03error.jsp" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%-- 4.지시자 (directive) 생김새 : <%@ %>

- 4.1 page 지시자 : 주로 가장 상단에 작성, JSP 내에서 환경설정을 담당하기도 함
	- import 도  page 지시자로 작성
	- 이동할 페이지 지정 (에러페이지)
- 4.2 include 지시자 
- 4.3 taglib 지시자
 --%>
 <% ArrayList<Integer>  List1 = new ArrayList<Integer>();
 
 int result = 2/0;
 //0으로 나눌 시 zero divide eror
 
 %>
 
 
</body>
</html>