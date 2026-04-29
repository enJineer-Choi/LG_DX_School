<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<form action="JoinCon.do" method="post">
		
		<table border="1">
			
			<tr>
				<td>ID : </td>
				<td><input type="text" name="id"></td>
			</tr>
			<tr>
				<td>PW : </td>
				<td><input type="password" name="pw"></td>
			</tr>
			<tr>
				<td>NICK : </td>
				<td><input type="text" name="nick"></td>
			</tr>
			
			<tr>
				<td><input type="submit" value="회원가입"></td>
			</tr>
			
		</table>
		
	
	</form>



</body>
</html>