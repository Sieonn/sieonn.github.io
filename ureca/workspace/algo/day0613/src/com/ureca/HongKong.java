package com.ureca;

public class HongKong implements MenuPan {
	public void 짜장면() {
		System.out.println("도와줘요 짜장면~");
	}//접근제어자를 부모와 같거나 큰 접근제어자를 설정해 주어야한다.
	//인터페이스는 앞에 기본으로 퍼블릭을 안써줘도 퍼블릭이니 얘는 퍼블릭 이상을 써줘야함

	@Override
	public void 짬뽕() {
		System.out.println("매콤한 짬뽕~");
	}

	@Override
	public void 볶음밥() {
		
	}
	public void 초밥() {
		
	}
}
