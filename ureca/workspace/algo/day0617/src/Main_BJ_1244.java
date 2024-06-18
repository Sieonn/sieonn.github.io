import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main_BJ_1244 {

	public static <K, V> void main(String[] args) throws Exception {
//		Scanner sc = new Scanner(System.in);
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		int swno = Integer.parseInt(br.readLine());
		String str = br.readLine();
//		StringTokenizer tokens =  new StringTokenizer(str," ");
		String[] strArr = str.split(" ");
		
		int studno = Integer.parseInt(br.readLine());
		int [][] studArr = new int [studno][2];
		for(int i = 0; i<studno; i++) {
			String str2 =  br.readLine();
			StringTokenizer token2 =  new StringTokenizer(str2," ");
			for(int j=0; j<2; j++) {
				studArr[i][j]= Integer.parseInt(token2.nextToken());
			}
		}
		for(int i =0; i<studArr.length; i++) {
			for(int j = 1; j<swno+1; j++)
			if(studArr[i][0]==1 && j%studArr[i][1]==0) {//남학생
				if(strArr[j-1].equals("1")) {
					strArr[j-1]="0";
				}else {
					strArr[j-1]="1";
				}
				
			}else if(studArr[i][0]== 2){
				int v = studArr[i][1]+1;
				for(int k=1; k>swno/2; k++) {
					if(v-k >= 0 && v+k <= swno-1) {
						if(strArr[v-k].equals(strArr[v+k]) &&
								strArr[v-k]=="1") {
							strArr[v-k]="0";
							strArr[v+k]="0";
						} else if(strArr[v-k].equals(strArr[v+k]) &&
								strArr[v-k]=="0") {
							strArr[v-k]="1";
							strArr[v+k]="1";
						}
					}
				}
				
			}
			
		}
		 System.out.print("strArr 배열 내용: ");
	        for (int i = 0; i < strArr.length; i++) {
	            System.out.print(strArr[i] + " ");
	        }
	        System.out.println(); // 줄 바꿈

	        br.close();

	}

}
// 01010001
// 01110101

