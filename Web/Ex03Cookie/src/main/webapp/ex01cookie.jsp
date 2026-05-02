
<%@page import="java.net.URLEncoder"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<!-- Cookie(쿠키)란?
- 데이터를 저장하는 영역 
- "클라이언트"에 저장하는 정보 > 
- 서버에 부하가 적음 
- 단점 : 보안에 취약 ,작은용량만 허용 (사이트당 20개, 개당 최대 4byte까지만 저장가능)
- 데이터의 기간 설정이 가능 (사이트마다 다름)
 
쿠키 사용 예시
- 일주일간 보지 않기
- 최근 본 목록 
- 장바구니 

- scope는 데이터를 주고받는 영역의 데이터
 -->
 
 <h1>Cookie 생성 페이지</h1>
 
<% //1.쿠키 객체 생성

// Cookie는 default 생성자가 존재하지 않음
// 매개변수로 name과 value값을 가지고 있음 > 둘다 String type
// * 주의사항 : value값에 공백, 특수문자는 불가능!!(단, 가능하게 하는 방법 존재)
// 공백이 존재하면 500Error가 발생함!

//공백과 특수문자 처리 방법
//인코딩을 통해서 가능 한국말 처리 희망시 UTF-8
String data = URLEncoder.encode("hello World!","UTF-8");

Cookie  cookie = new Cookie("first",data);

// 

 
// 2.기간설정 -> int로 작성 (작성한 int의 단위는 초)
cookie.setMaxAge(60);//즉 1분의 기간 설정
// 1년 저장 하고 싶을 때 : 60 * 60 * 24 * 365 (연산 가능 int형이므로)
 
//객체만 생성한다고 Cookie가 만들어지는 것은 아님

// 3. Cookie 저장 -> 
// Server가 Client한테 Cookie를 저장하라고 말해줘야함 (그래서 response를 사용해야함)

response.addCookie(cookie);

%>

<a href = "ex01cookie2.jsp">쿠키 확인 페이지</a>
 
 
 
</body>
</html> 