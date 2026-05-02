<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String name = request.getParameter("name");
	

%>

<fieldset>
		<legend>학점 확인 프로그램</legend>
		
			<table>
				<tr>
					<td>이름</td>
					<td><%=name %></td>
				</tr>
				<tr>
					<td>Java점수</td>
					<td></td>
				</tr>
				<tr>
					<td>HTML/CSS점수</td>
					<td></td>
				</tr>
				<tr>
					<td>Python 점수</td>
					<td></td>
				</tr>
				
				<tr>
					<td>평균</td>
					<td></td>
				</tr>
				<tr>
					<td>학점</td>
					<td><strong></strong></td>
				</tr>
 
			</table>
		
	</fieldset>
 
</body>
</html>