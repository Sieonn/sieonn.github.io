package com.ureca;

import java.util.Random;

public class LottoNumGenTest {

	public static void main(String[] args) {
		//1~45 숫자 중 6개 번호 뽑아오기
	   int[]lotto = new int[6];//[0]번지~[5]번지 생성
	   //int[]lotto = {0,0,0,0,0,0};
	   //랜덤수
	  /*
	   Math.random() ==> 0.000 ~ 0.99999 * 10 
                       (int) 0.000 ~ 0.99999  ==> 0 
                       0.000 ~ 0.99999 * 10                 
                       (int) 0.000 ~  9.99999 ==> 0~9  + 1  ==> 1~10
                                         
	   */
//	   lotto[0]=  (int)(Math.random()*45) + 1; //1~45
	   
	   Random r = new Random(); 
	     //r.nextDouble(); ==> Math.random()과 동일한 메서드
	     lotto[0]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	   
	  do { 
	     lotto[1]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	    }while(lotto[1]==lotto[0]);//중복된 수가 발생했다면
	  
	  do { 
		  lotto[2]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	  }while(lotto[2]==lotto[1] || lotto[2]==lotto[0]);//중복된 수가 발생했다면
	  
	  do { 
		  lotto[3]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	  }while(lotto[3]==lotto[2] || lotto[3]==lotto[1] || lotto[3]==lotto[0]);//중복된 수가 발생했다면

	  do { 
		  lotto[4]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	  }while(lotto[4]==lotto[3] || lotto[4]==lotto[2] || lotto[4]==lotto[1] || lotto[4]==lotto[0]);//중복된 수가 발생했다면

	  do { 
		  lotto[5]= r.nextInt(45)+1; //0~44 +1 ==> 1~45
	  }while(lotto[5]==lotto[4] || lotto[5]==lotto[3] || lotto[5]==lotto[2] || lotto[5]==lotto[1] || lotto[5]==lotto[0]);//중복된 수가 발생했다면
	   
	  for (int i = 0; i < lotto.length; i++) {
		System.out.print(lotto[i]+" ");
	   }
	  
	}//main
	
}//end class











