package com.lguplus;

//class B{}
public class MethodCallTest {
	static void good() {  
		System.out.println("프론트엔드 좋아요");
	}
	
	static class B{// 내부클래스
		
	}
	
	public static void main(String[] args) {
		System.out.println("안녕, 유플러스 ^o^");
		
		A.uplus(); //static  멤버는 클래스명으로 접근
				//클래스명.메서드();
		
		A a = new A();
		a.hello(); //클래스 멤버는 참조변수로 접근
				//참조변수(레퍼런스변수).멤버메서드
		good();
	}//main


}
