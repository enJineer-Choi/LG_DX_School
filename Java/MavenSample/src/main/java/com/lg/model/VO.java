package com.lg.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

//@Data : Data annotation이 모든 메소드를 다 생성해줌 (getter,setter,기본생성자, toString())

@AllArgsConstructor //모든 인자를 사용해서 생성자를 만듦
@NoArgsConstructor //기본 생성자 메소드
@RequiredArgsConstructor // 필요한 인자를 받는 생성자 메소드

@Getter
@Setter
//getter,setter


public class VO {
	@NonNull
	private String id;
	@NonNull private String pw;
	private String nick;
	

//	lombok으로 새로 정리할 예정
//	//회원가입용 생성자 메소드
//	public VO(String id, String pw, String nick) {
//		super();
//		this.id = id;
//		this.pw = pw;
//		this.nick = nick;
//	}
//	//로그인용 생성자 메소드
//	public VO(String id, String pw) {
//		super();
//		this.id = id;
//		this.pw = pw;
//	}
//
//	public String getId() {
//		return id;
//	}
//
//
//	public String getPw() {
//		return pw;
//	}
//
//
//	public String getNick() {
//		return nick;
//	}


	
	
	
	
	
}
