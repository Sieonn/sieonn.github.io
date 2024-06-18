package com.ureca;

public class Abc {
	int su;  //== int su=0;
//	My my; // == My My=null; //클래스 데이터 값들은 기본값이 null이다.
	String str;
	
	Abc() {//매개변수가 비이있는것을 생성자라고 하는데 클래스와 이름이 같고
			//리턴타입이 없기 때문에 기본생성자라고 말할수 있다.
			//: 초기화 메서드
		this("ureca"); //다른 생성자 호출시 첫번째 문장으로 호출해야함
		su =1000;
//		my= new My();
	}
	Abc(String str){ //오버로딩 생성자 : 이름은 같은데 파라미터가 다른경우
					//String str: 지역변수
		this.str=str;
		
	}
	//멤버에서 선언된 변수의 이름과 지역변수의 이름이 같아도 사용할 수있는 지역이 달라서 허용한다.

	void hello() {
		System.out.println("안녕");
	}//메서드안에 지역변수 선언, 지연변수 초기화, 메소드 호출
}
