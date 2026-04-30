package com.lg.database;

import java.io.IOException;
import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class SqlSessionManager {

	// SqlSessionFactory : 기능을 할 때마다 해당 세션을 열어줄 세션공장
	public static SqlSessionFactory sqlSessionFactory;

	static {
		
		String resource = "com/lg/database/mybatis-config.xml"; 
		Reader reader;
		try {
			reader = Resources.getResourceAsReader(resource);
			
			sqlSessionFactory = new SqlSessionFactoryBuilder().build(reader);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	// DAO클래스에서 호출할 메소드
	public static SqlSessionFactory getSqlSession() {
		return sqlSessionFactory;
	}
	
	
	
}
