package com.lguplus;

//import java.io.IOException;

public class InputTest {

	public static void main(String[] args) throws Exception {// throws IOException {
		System.out.print("한 자리 수를 입력하세요:");
		int su = System.in.read()-'0'; //'0' = 아스키코드값:48
		
		
		//enter키 처리를 해주는 문장
		System.in.read(); //CR 13
		System.in.read(); //LF 10
		
		
		System.out.println("입력된 수 = " + su);
		
		
		System.out.print("동일한 수를 입력하세요:");
		int su2 = System.in.read();
		System.out.println("그 수의 아스키 코드 = " + su2);
	}

}

//