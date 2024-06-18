package com.ureca;

public class Child extends Parent{
                  //is a  : 자식은 부모다 ==> 자식클래스는 부모클래스로 형변환이 가능하다
					// 부모클래스에 선언된 곳에 자식이 가도된다.
					//자식이 정의한 메소드를 부모가 호출할 수 없음!!!!!
   void print() {//오버라이딩 (메소드 재정의)
	   System.out.println("자식");
   }
   

}
