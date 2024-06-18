package com.uplus;

public class LeapYearTest {

	public static void main(String[] args) {

		/*
		 * <윤년의 조건>
		 * 
		 * 1. 연도를 4로 나누어 나머지가 0이고 연도를 100 으로 나누어 나머지가 0이 아닌 경우.
		 * 
		 * 2. 연도를 400으로 나누어 나머지가 0인 경우.
		 * 
		 * 실행결과) ==> 조건을 만족했을때 true 출력 ==> 조건을 만족하지않았을때 false 출력
		 */
		int year = 2024;
		boolean b1 = (year % 4) == 0;
		boolean b2 = (year % 100) != 0;

		boolean b3 = (year % 400) == 0;

		System.out.println((b1 && b2) || b3);
	}
}
