<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<!--  JSP 내에서 자바코드 작성 
*HTML 주석 안에 모양새 작성 안됨(주석 안에 있어도 인식해버림)
1. 스크립틀릿
<%--여기서는 기호 사용가능(JSP 전용주석)
1. 스크립틀릿 (<% %>)
- 자바코드로 인식하고 싶은 부분만 `스크립틀릿` 태그를 씌워주면 됨!

2. 표현식 (<%=%>) : 변수나 메소드, 객체 등 화면에 출력하고 싶을 때 사용 (단순 출력)


--%>
-->

<% 
// 자바 코드로 인식
int num1 = 115;
//반복문, 조건문 사용 가능
if(num1%2 ==0){%>
	
	 <h1> <%=num1%>은 짝수입니다. </h1>
<% }else{%>
	<h1> <%=num1%>은 홀수입니다. </h1>
<% }
%>




</body>
</html>