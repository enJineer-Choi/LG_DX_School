<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>Session 확인페이지!</h1>

<!-- Seesion
브라우저가 종료되기 전까지 클라이언트의 정보를 저장하는 기술
-> "서버"에 저장
서버에서는 중복되지 않는 SessionId를 클라이언트에게 발급하여 사용자를 식별

장점
- 보안 유지
- 서버의 용량을 사용하고 있기 때문에 별다른 제한이 없음
- 웹 브라우저에 의존하지 않고 한번에 많은 정보를 저장 가능

단점 
- 저장하는 양이 많아지면 서버에 부하가 커짐 


Scope에서 나왔던 Session과 똑같은 개념임!!


 -->
<%
//쿠키는 공백,특수문자 구분
//하지만 세션은 상관없음 (인코딩 필요X)
//session의 경우에는 Cookie와 다르게 모든 타입 작성이 가능!
	session.setAttribute("test","hello world");
	session.setAttribute("age",20);
	
	String s = (String)session.getAttribute("test");
	int age = (int)session.getAttribute("age");
	//사실 int는 클래스가 아닌데, 이게 가능한 이유는
	// object -> Integer -> int 로 변환됨.

	
%>

세션 test 출력 : <%=s %> <br>
세션 age 출력 : <%= age %> <br>

<%
	//세션값 수정하기
	//session도 name값 중복을 허용하지 않음 > 같은 name값 작성시 데이터 변경
	
	
	session.setAttribute("test","안녕");
	s = (String)session.getAttribute("test");
	
	
%>

수정된 test 출력 : <%=s %> <br>

<a href = "ex04delete.jsp">세션 삭제 페이지 이동</a>

</body>
</html>