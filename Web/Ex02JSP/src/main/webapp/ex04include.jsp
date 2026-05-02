<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%--include 지시자
: 현재 페이지에 다른 페이지를 포함시킬 때 사용하는 구성요소
주로 header, footer로 사용(고정영역) : 다른 페이지에 동일하게 적용시킬 수 있음
- 유지보수 편리
 --%>
 <h1>메인페이지 입니다.</h1>
 
 <%@include file = "ex04footer.jsp" %>

</body>
</html>