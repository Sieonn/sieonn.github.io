import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_BJ_1244_스위치켜고끄기3 {
/*
  
 br.readLine() => 각줄마다 실행
 
8                       => "8"                ==> Integer.parseInt("8") ==> 8
0 1 0 1 0 0 0 1         => "0 1 0 1 0 0 0 1"
                             =>Integer.parseInt("8")   : 8
                             =>Integer.parseInt("123") : 123
                             =>Integer.parseInt("12a") : 에러 NumberFormatException
                             =>Integer.parseInt("1 0") : 에러 NumberFormatException

String str="0 1 0 1 0 0 0 1";
StringTokenizer tokens = new StringTokenizer(str," ");
   ==> tokens = ["0", "1", "0", "1", "0", "0", "0", "1",];
for(스위치의 범위){
       Integer.parseInt(tokens.nextToken());// "0" => 0
}

2                       => "2"               ==> Integer.parseInt("2") ==> 2
1 3                     => "1 3"

str="1 3"
tokens = new StringTokenizer(str); //두번째 인자값 구분자를 생략하면 " "값이 기본값으로 들어감
 ==> tokens=["1", "3"];
        Integer.parseInt(tokens.nextToken());// "1" => 1
        Integer.parseInt(tokens.nextToken());// "3" => 3


2 3                     => "2 3"

 */
	
	public static void main(String[] args) throws Exception{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	  int N = Integer.parseInt(br.readLine());//스위치 개수      

      int[] switchArry = new int[N+1];//스위치정보를 담을 배열   
	  //입력되는 스위치 정보가 1부터 사용되기 때문에  
	  // ==> 배열의 0번지를 버림으로써  입력값과 배열번지를 일치시켜준다!!
      
	  StringTokenizer tokens = new StringTokenizer(br.readLine()," ");//"0 1 0 1 0 0 0 1"
      for (int i = 1; i <= N; i++) {
		  switchArry[i] = Integer.parseInt(tokens.nextToken()); //스위치정보 입력	
	  }

      //데이터 입력 확인
//      System.out.println(Arrays.toString(switchArry));

	  int stuNum = Integer.parseInt(br.readLine());//학생수
	  
	  for(int i=0; i<stuNum; i++) {//학생수만큼 반복
		  tokens = new StringTokenizer(br.readLine()," ");//"1 3"   "2 3"
		  int gender = Integer.parseInt(tokens.nextToken());//학생의 성별
		  int startNum = Integer.parseInt(tokens.nextToken());//스위치 시작번호
		  
		  if(gender==1) {//남학생 : 시작번호를 기준해서 배수를 스위치
			  for(int j=startNum; j<=N; j+=startNum) {//j++  j=j+1
				                     //j+=startNum  j=j+startNum
				 //삼항 연산자 :   변수명 = (조건식) ? A : B;
				 //         A=> 참일때리턴값 , B=> 거짓일때 리턴값 
				  switchArry[j] = switchArry[j]==0 ? 1:0; 
				                 //현재 스위치 값이 0이라면 1을 리턴
				  
			  }
		  }else {//여학생: 시작번호를 기준해서 (좌우)대칭되는 가장 가까운 수부터 스위치, 비대칭 전까지
			  //좌우 비교할 길이가 다를 수 있으므로 최소 비교 길이를 구하자!!
			  int limit=startNum;
			  if(N-startNum+1  < startNum) {
				  limit = N-startNum+1;
			  }					  

			  //1.선택된 스위치는 무조건 변경
			  switchArry[startNum] = switchArry[startNum] == 0 ? 1 : 0;
			  
			  for(int j=0,left=startNum-1,  right=startNum+1;  
					  j<limit-1;  
					  j++, left--, right++) {
				  //반복횟수j, 좌우인덱스 left,right
				  // 왼쪽으로 진행형대칭 left,  오른쪽으로 진행형대칭 right,  전체비교횟수 j
				  
				  if(switchArry[left] != switchArry[right]) break; //좌우 대칭이지 않다면 종료
				  
				  switchArry[left] = switchArry[left] == 0 ? 1 : 0;
				  switchArry[right] = switchArry[right] == 0 ? 1 : 0;
				  
			  }
		  }//여학생 스위치
		  
		  
		  
	  }//for
	  
	  //스위칭 결과를 출력
	  for(int i=1; i<=N; i++) {//스위치 인덱스 표현
		  System.out.print(switchArry[i]+" ");
		  if(i%20==0)System.out.println();//줄바꿈
	  }
      br.close();
	}//main

}//end clas