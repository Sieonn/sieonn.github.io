package com.lguplus;

import java.util.Arrays;

public class MissonArrayTest {

	public static void main(String[] args) {
		int[] su = { 1, 2, 3, 4, 5 };
		System.out.println(su[0]);
		System.out.println(su[1]);
		System.out.println(su[2]);
		System.out.println(su[3]);
		System.out.println(su[4]);

		// 배열 == 객체(필드, 메서드 포함)
		// 자바배열 ==> length속성(필드)
		for (int i = 0; i < su.length; i++)
			System.err.print(su[i] + " ");

		System.out.println();
		// 나는 인덱스에 관심없고 데이터에만 관심이 있다.
		// ==> 개선된 for문 (forEach문)을 사용
		// ==> 형식) for(자료형 변수명: 배열명){}

		System.out.println("==================");
		for (int data : su) // 배열 인덱스 표현
			System.err.print(data + " ");
		System.out.println();

//		int [] su3;
//		su3 = su;
//		int[] su3 = new int[su.length];
		// 깊은 복사(다른 메모리를 할당, 배열 각가그이 번지내의 데이터를 복사)
//		for(int i=0; i<su.length; i++) {
//			su3[i] = su[i];
//		}

		// 깊은 복사: object.clone(); //Object는 최상위 클래스
//			System.arraycopy(); ==> 속도가 빠르다.
		
//		  int[] su3 = su.clone(); 
//		  int []su3 = System.arraycopy(Object src(누구를), 
//				  int srcPos(어디서부터 복사해서),Object dest(어디에),
//				int destPos(어디부터 붙여넣는데),
//				int lenght(배열이 가지고 있는 요소의 갯수 , 할당된 방의 크기));
//		System.arraycopy(su, 0, su3, 0, 0);
//		== int  []su3 = Arrays.copyOf(su,su.length);

		int  [] su3 = Arrays.copyOf(su,su.length);
		
		
//		Arrays.copyOfRange(배열Oriainal,시작인덱스from, 복사할 길이 to)
//		int [] su3 = Arrays.copyOfRange(su3, 0, su.length);
//		System.arraycopy(); 메소드를 편리하게 사용하도록 만든 메소드
 		
		//배열의 값만 (for문을 사요하지 않고) 쉽게 출력
		//==> java.util.Arrays.toString(배열);
		System.out.println("su3배열>>>"+Arrays.toString(su3));
		System.out.println("su3배열>>>"+su3); 
		System.out.println("su배열>>>"+Arrays.toString(su)); //2차원 안됨. 1차원만 2차원은 분해해서 to string 사용
		
		System.out.println("#su3배열 데이터 출력!#");
		for (int data :  su3) {
			System.out.println(data);
		}
		 su3[2] = 33;
		System.out.println("#su3[2]번지 데이터 출력=>" +  su3[2]);
		System.out.println("#su[2]번지 데이터 출력=>" + su[2]);
		System.out.println("===================== 따로 메모리 할당을 해줘야한다.");
		
//		su= {1,2,3,4,5}; == 변경==> su{5,4,3,2,1}

		//swap 작업
//		su[0] =su[4];
//		su[1] = su[3];
//		i		j
		
//		temp =a;
//		a =b;
//		b= temp;
		
		System.out.println("\n5번문제");
		int half = su.length/2;
		int temp;
		for(int i = 0, j=su.length-1;i<half;i++,j--) {
			temp = su[i];
			su[i] = su[j];
			su[j] = temp;
		}
		for(int i=0; i<su.length; i++) {
			System.out.print(su[i]+" ");
		}
	}// main
}
