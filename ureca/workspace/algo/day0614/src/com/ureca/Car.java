package com.ureca;

public class Car {
	
   //멤버변수 == 필드  ==> 초기값이 존재   ( 정수0, 실수0.0,  논리false, 문자 '\u0000', null)
    String carName;//null String carName=null;
    int wheelNum;//0
    int velocity;//0
    
//    public Car() { //기본생성자

//	}// 기본생성자를 작성해놓으면 선언하면 초기값이 ( 정수0, 실수0.0,  논리false, 문자 '\u0000', null)을 가지고 시작한다.
    

	public Car(String carName, int wheelNum, int velocity) { //오버로딩 생성자
		super(); //Object의  기본 생성자 호출
		this.carName = carName;
		this.wheelNum = wheelNum;
		this.velocity = velocity;
	}
	
	public String toString() {//to~()메소드: 변환메소드
		                      //toString()메소드 : 객체의 상태를 표현하는 메소드
		String str="이 차는 "+ this.carName +"이고 바퀴수는 "+ wheelNum+", 속도는 "+ velocity+"입니다!!";
		return str;
	}
	
// alt +shift +s	
//	@Override
//	public String toString() {
//		return "Car [carName=" + carName + ", wheelNum=" + wheelNum + ", velocity=" + velocity + "]";
//	}
	
	public boolean equals(Car ob) {
					// Object c =new Car("소나타", 4, 100);
		Car c = (Car)ob;
		if(
//		  carName == c.carName  &&
		  carName.equals(c.carName)  && //String은 클래스이므로 equals로 비교
		   wheelNum == c.wheelNum  &&
		   velocity == c.velocity) {
			return true;
		}
		return false;
	}//equals
	

	public static void main(String[] args) {
		// Car - 클래스 객체  :  ★객체 비교법!!   1.내용 비교   2.메모리(주소) 비교
		
		Car c1 = new Car("소나타", 4, 100);
//		Car c2;
//		    c2 = c1;//메모리 주소 복사
		
		System.out.println(c1.toString());
		
		Car c2 = new Car("아반떼", 4, 100);
		
//		c1==c2  : 레퍼런스비교, 메모리비교(같은 메모리를 사용하는지?)
		if(c1==c2) {
			System.out.println("객체(메모리)주소 같음!!");
		}else {
			System.out.println("객체(메모리)주소 다름!!");
		}
		
//		c1.equals(c2)	: 객체 내용비교, 속성(필드)비교
		if(c1.equals(c2)) {
			System.out.println("객체내용 같음!!");
		}else {
			System.out.println("객체내용 다름!!");
		}
		
	}//main
    
    
    
    
    
}
