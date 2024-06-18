package com.ureca;

import java.util.Arrays;
import java.util.Random;

public class LottoNumGenTest2 {

	static int[]lotto = new int[6];//[0]번지~[5]번지 생성

	public static boolean isDuplicateNum(int index) {//중복된 수가 발생한다면 리턴 true
	   	for(int i=index-1; i>=0; i--) {
	   	   if(lotto[index] == lotto[i]) return true;
	   	}
	   	return false;
	}//isDuplicatNum
	
	public static void main(String[] args) {
		//1~45 숫자 중 6개 번호 뽑아오기
	   //랜덤수
	   
	   Random r = new Random(); 
	     //r.nextDouble(); ==> Math.random()과 동일한 메서드
	System.out.println("★★ 금주 행운의 로또번호 ★★");   
	for(int no=1; no<=5; no++) {   
	   for(int i=0; i<lotto.length; i++) {
	     lotto[i]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	     if(isDuplicateNum(i)) i--;
	   }
	   
//	   for (int i = 0; i < lotto.length; i++) {
//			System.out.print(lotto[i]+" ");
//		}
//	   System.out.println();
	   Arrays.sort(lotto);
	   System.out.print(no+ "회: ");
	   for (int i = 0; i < lotto.length; i++) {
			System.out.print(lotto[i]);
			if(i < lotto.length-1 )System.out.print(", ");
	   }
	   System.out.println();
	}
	   
	}//main
	
}//end class











