<%@page import="java.net.URLDecoder"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
 
<style>
#list {
	width: 200px;
	height: 400px;
	background-color: yellow;
	text-align: center;
	position: fixed;
	right: 0px;
	top: 300px;
}
</style>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div>
 
 
		<form action="Shop" method="post">
			<h1>인기 판매 물품</h1>
 
			<table border=1>
				<tr>
					<td>상품 1 : 갤럭시 핸드폰</td>
					<td>상품 2 : 갤럭시 탭</td>
					<td>상품 3 : 갤럭시 버즈</td>
					<td>상품 4 : 갤럭시 워치</td>
					<td>상품 5 : 갤럭시 북</td>
				</tr>
				<tr>
					<td><input type="checkbox" name='product' value="갤럭시핸드폰"></td>
					<td><input type="checkbox" name='product' value="갤럭시탭"></td>
					<td><input type="checkbox" name='product' value="갤럭시버즈"></td>
					<td><input type="checkbox" name='product' value="갤럭시위치"></td>
					<td><input type="checkbox" name='product' value="갤럭시북"></td>
				</tr>
				<tr>
					<td>상품 1 : 아이폰</td>
					<td>상품 2 : 아이패드</td>
					<td>상품 3 : 에어팟</td>
					<td>상품 4 : 애플워치</td>
					<td>상품 5 : 맥북</td>
				</tr>
				<tr>
					<td><input type="checkbox" name='product' value="아이폰"></td>
					<td><input type="checkbox" name='product' value="아이패드"></td>
					<td><input type="checkbox" name='product' value="에어팟"></td>
					<td><input type="checkbox" name='product' value="애플위치"></td>
					<td><input type="checkbox" name='product' value="맥북"></td>
				</tr>
 
				<tr>
					<td colspan=5><input type="submit" value="담기"></td>
				</tr>
 
			</table>
 
		</form>
 
	</div>
	<div id="list">
		<%
			Cookie[] cookies = request.getCookies();
			if(cookies != null){
				//쿠키가 담겨 있다는 뜻
				for(int i = 0;i<cookies.length;i++){
					if(cookies[i].getName().contains("item")){					
						out.print(URLDecoder.decode(cookies[i].getValue(),"UTF-8")+"<br>");
					}
					
				}
				//쿠키가 JSessionID만 있는 경우에도 선택하신 물건이 없습니다 라고 출력하기!
				if(cookies.length ==1 && cookies[0].getName().equals("JSESSIONID")){
					out.print("선택하신 물건이 없습니다.");
				}
			}else{
				out.print("선택하신 물건이 없습니다");
			}
		
		
		
		%>
		
		
		
		
		
	</div>
</body>
</html>
 	