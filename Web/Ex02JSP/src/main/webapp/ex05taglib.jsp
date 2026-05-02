<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%--taglib 지시자 : 라이브러리를 태그로 사용하겠다라는 의미
- 위코드의 의미 jstl이라는 라이브러리를 c라는 태그로 사용하겠다
JSTL : JSP Standard Tag Library

-> tag를 사용해서 jsp를 편하게 쓰자
-> 장점 : 코드의 단순화.
-> 단점 : 문법이 새롭게 존재. (JSTL 문법 따로 존재) 
 --%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<!-- taglib 사용하기 전 문법 -->
<% //for문을 활용하여 Hello world! 10개 출력
for (int i=0;i<10;i++){%>
	<h1>Hello world</h1>
<%}
%>


<!-- taglib 사용문법 -->
<c:forEach begin="1" end="10" step="1">
<h1>안녕하세요!</h1>
</c:forEach>

<!-- if문(단순 if문 : else,else if 가 존재하지 않음 > 다른 문법 사용필요!) 
test에 조건식 작성-->

<%-- <% int num1 = 9; %>
이건 JSP에서 사용하고 있는 num1을 선언해서 인식하지 못함
--%>

<!-- 따라서 밑의 코드처럼 jstl이 이해할 수 있는 변수로 선언! -->
<c:set var="num1" value="9" />
<c:if test="${num1%2 ==0 }">
<h1>짝수입니다</h1>
</c:if>

<!-- choose - when 문 : 
choose : 조건문의 문단을 구분짓는 역할
when : 조건식을 작성하여 조건에 맞는 코드 실행
otherwise : else 나머지 경우의 수
-->

<c:choose> 

<c:when test="${num1%2==0 }">
<h1>짝수입니다</h1>
</c:when>

<c:when test="${num1%2==1 }">
<h1>홀수입니다</h1>
</c:when>

<c:otherwise>
<h1>숫자가 아닙니다!</h1></c:otherwise>
</c:choose>

</body>
</html>