package Study;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Test {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine(); //0 1 0 0 1입력
		// str="0 1 0 0 1"
		StringTokenizer tokens = new StringTokenizer(str, " ");
		int[]arr=new int[5]; //정수 데이터들을 담을 빈 배열 생성
		 for(int i=0; i<5; i++){
		 	arr[i] = Integer.parseInt(tokens.nextToken());
		 	System.out.println(Arrays.toString(arr));
		System.out.println(Arrays.toString(arr));
		 }
	}
}
