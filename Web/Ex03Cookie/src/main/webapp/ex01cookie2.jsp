<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.net.URLDecoder" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>쿠키에 저장된 값 가지고 오기!</h1>

<%

	//생성 된 쿠키 가지고 오기!
	//생성할 때 응답 요청이 끝나서 더이상 저장 되어 있지 않음 -> 즉, 다시 server에
	//요청해줘야함 .  "Request"를 해줘야함
	Cookie [] cookies = request.getCookies();
	
	//객체 안에 담긴 name값 가지고 오는 메소드 = getName();
	// value 값 가지고 오는 메소드 = getValue();
	for (Cookie c : cookies){
		//out.print(c);//jakarta.servlet.http.Cookie@1e12dd7ajakarta.servlet.http.Cookie@789da8ba
		//다음과 같은 객체 값으로 출력
		
		//현재 문제점 : URLEncode 활용하여 띄어쓰기, 특수문자 처리 완료
		//c.getValue를 출력해봣더니 Encoding한 결과값을 출력
		//원 데이터로 출력하기 위해 디코딩을 진행
		String decodeValue = URLDecoder.decode(c.getValue(),"UTF-8");
		out.print(c.getName()+ " : "+decodeValue+"<br>");
		
	}
	



%>



</body>
</html>