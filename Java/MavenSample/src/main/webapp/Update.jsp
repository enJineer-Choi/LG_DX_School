<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<form action="UpdateCon.do" method="post">
		
		<table border="1">
			
			<tr>
				<td>ID : </td>
				<td><input type="text" name="id" value="${vo.id}" readonly></td>
				<!-- 오직 읽을 수만 있게 아이디 수정 불가능하도록-->
			</tr>
			<tr>
				<td>PW : </td>
				<td><input type="password" name="pw" required></td>
				<!--  비밀번호가 비어있게 db에 전달되지 않도록 required 속성 -->
			</tr>
			<tr>
				<td>NICK : </td>
				<td><input type="text" name="nick" value = "${vo.nick}"></td>
			</tr>
			
			<tr>
				<td><input type="submit" value="수정하기"></td>
			</tr>
			
		</table>
		
	
	</form>



</body>
</html>