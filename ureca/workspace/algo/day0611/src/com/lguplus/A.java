package com.lguplus;

public class A{
	void hello(){
		System.out.println("A클래스 안녕~");
	}
	static void uplus() {
		System.out.println("LG U+!");
	}
}
class B{} //이미 같은 패키지 안에 B라는 이름의 클래스가 존재하기 때문에
			//중복 오류가 발생합니다.