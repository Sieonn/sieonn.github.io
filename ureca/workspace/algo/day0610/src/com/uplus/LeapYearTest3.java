	package com.uplus;

import java.util.Scanner;

public class LeapYearTest3 {

	public static void main(String[] args) {
		//java.lang => 기본 패키지
		//java.lang.String java.lang.System
		//현클래스와 동일한 패키지에 있는 클래스 또는 기본패키지에 있는 클래스는 바로 사용이 가능!
		//==> 이외의 클래스는 import가 필요: 클래스의 위치를 표현하는 방법!
		//java.util.Scanner ==> import java.util.Scanner;
		
		//Scanner는 첫글자 대문자니까 클래스!
		Scanner sc = new Scanner(System.in);
		
		int year = sc.nextInt();
//		int year =  //2024;
		boolean b1 = (year % 4) == 0;
		boolean b2 = (year % 100) != 0;

		boolean b3 = (year % 400) == 0;
			
		if((b1 && b2) || b3) {
			System.out.println(year+"년은 윤년입니다."); //"2024는 윤년입니다."
		}else {
			System.out.println(year+ "년은 평년입니다.");
		}
//		System.out.println((b1 && b2) || b3);
	}//main
}//class end
