package com.lguplus;

public class ArrayTest1 {
	public static void main(String[] args) {
		int [] su = {1,2,3,4,5};
//		for(int i= 0; i<5; i++) {//배열 인덱스 표현
//		for( int i=0; i<su.length; i++) {// 배열 인덱스 표현
		
		int n = su.length;
		for(int i=0; i<n; i++) {// 배열 인덱스 표현
			System.err.print(su[i]+ " ");
		}
	}
}
			