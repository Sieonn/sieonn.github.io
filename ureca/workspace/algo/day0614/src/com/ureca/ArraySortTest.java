package com.ureca;
import java.util.Arrays;

public class ArraySortTest {
   public static void main(String[] args) {
	   int[]su= {13, 8, 7, 10, 100, 5};
//	   ==> 정수 배열을 오름차순 정렬하시오. 
	   /*
	   
       i[0   1  2   3   4]           비교대상 왼쪽 데이터(인덱스)
       j    [1  2   3   4   5]       비교대상 오른쪽 데이터(인덱스)
       
int[]su= {13, 8, 7, 10, 100, 5};
         ↑ > ↑
         8   13 7  10  100 5  
         ↑      ↑
         7   13 8  10  100 5
         ↑          ↑ 
         7   13 8  10  100 5
         ↑              ↑                 
         7   13 8  10  100 5
         ↑                 ↑                   
         5   13 8  10  100 7
         ==> 한 사이클 (i=0일때 j값 변경하며 비교한 결과)   : 최소값을 맨 좌측으로 이동!!
         
*/	   
	   int temp;
	   for(int i=0; i<su.length-1; i++) {//기준: 비교왼쪽 번지데이터  (0~4)
		  for(int j=i+1; j<su.length; j++) {//비교오른쪽 번지데이터  (i+1 ~ 5)
			  //교환
			 if(su[i] > su[j]) { //오름차순 또는 내림차순
			  temp = su[i];
			  su[i] = su[j];
			  su[j] = temp;
			 }
		  }
	   }
	   
	   //정렬된 배열의 값을 확인  ===> Arrays.toString(1차원배열명);
	   System.out.println(Arrays.toString(su));
   }//main
}












