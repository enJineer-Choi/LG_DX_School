<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<!-- 3. session에 저장된 아이디값을 출력하면서 환영한다는 걸 보여주는 페이지 -->
<h1>메인 페이지</h1>

${sessionScope.id} 님 환영합니다.
<!--  스크립틀릿 열어서 getAttribute를 사용하지 않아도 간결하게 작성할 수 있음
훨씬 간결한 표현으로 작성가능 -->



</body>
</html>