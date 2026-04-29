<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix = "c" uri ="http://java.sun.com/jsp/jstl/core" %> 
<%-- <%@ taglib uri="jakarta.tags.core" prefix="c" %> --%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<%
		//자바 영역
		//현재 url을 통해서 쿼리스트링방식으로 result=success가 넘어오고 있음
		//request.getParameter("key");
		//String result = request.getParameter("result");
		
		//forwarding 방식으로 페이지 이동 후 값 가져오기
		//String result = (String) request.getAttribute("result");
	%>
	<a href="Join.jsp"><button>회원가입</button></a>
	<%--<%
	if(result!=null){
		if (result.equals("success")) {
			out.print("<h3>성공했습니다</h3>");
		}
	}
	--%>
	
	<!-- jstl 태그 라이브러리 -->
	<!-- request 영역의 값을 EL문법으로 가져올거임 -->
	<c:if test = "${!empty result }">
		<c:if test ="${result eq 'success' }">
			<h3>회원가입에 성공했습니다~!</h3>
		
		
		</c:if>
	</c:if>
	
	
	<a href="Login.jsp"><button>로그인</button></a>
	
	<!-- 1. 로그인을 안한 상태일때는 (session값이 없을경우) : 로그인을 해주세요
		2. 로그인을 한 상태일때는 (session값이 있을경우) : nick님 환영합니다~
		
		위 과정을 구현하고 싶음
	 -->
	
	<c:choose>
		<c:when test = "${empty vo }">
			<p>로그인 해주세요</p>			
		</c:when>		
		<c:otherwise>
			<p>${vo.nick}님 환영합니다~</p> <br>
			<!-- jstl에서 객체의 값을 가져오는 방법 객체.필드값 -->
			<!-- 개인정보수정과 회원탈퇴 두가지의 경우는 DB에 접근해야함! -->
			<a href = "Update.jsp"><button>개인정보 수정</button></a>
			
			
			<!-- 바로 DB에서 삭제하면 되므로 -->
			<a href = "DeleteCon.do"><button>회원탈퇴</button></a>
			
			
			
			<a href = "LogoutCon.do"><button>로그아웃</button></a>
			<!-- 
			
			로그아웃은 굳이 DB에 접근하지 않아도 되므로 바로 LogoutCon이라는 Controller에서 해결가능
			1. 로그아웃 버튼을 눌렀을때 Logoutcon이라는 servlet으로 이동
			2. 로그인했을때 세션에 저장한 값을 지우기
			3. Main.jsp 페이지로 이동 -->
			
			
			
			
			
			
		</c:otherwise>
	</c:choose>
	<!-- session으로 저장하기 때문에 이미 로그인에 성공하면 브라우저를 지우지 않는이상 
	데이터가 그대로 저장되어 있어서 계속 저장되어 있음. 
	 -->

</body>
</html>