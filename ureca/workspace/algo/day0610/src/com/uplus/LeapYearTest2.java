	package com.uplus;

public class LeapYearTest2 {

	public static void main(String[] args) {

		/*
		 * <윤년의 조건>
		 * 
		 * 1. 연도를 4로 나누어 나머지가 0이고 연도를 100 으로 나누어 나머지가 0이 아닌 경우.
		 * 
		 * 2. 연도를 400으로 나누어 나머지가 0인 경우.
		 * 
		 * 실행결과) ==> 2023년은 평년입니다. 또는 ==> 2023년은 윤년입니다
		 */
		int year = 2024;
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
