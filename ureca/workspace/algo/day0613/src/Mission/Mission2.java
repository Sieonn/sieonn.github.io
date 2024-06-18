package Mission;

import java.util.Arrays;
import java.util.Collections;

public class Mission2 {
	public static void main(String[] args) {
		char[]ch= {'J','a','v','A'};
		String[]names= {"홍길동", "길라임", "김주원"};
		int [] su = {13, 8, 7, 10, 100, 5};
		
//		Arrays.sort(ch);
//		Arrays.sort(names);
//		System.out.println(Arrays.toString(ch));
//		System.out.println(Arrays.toString(names));
		
		//API를 통해 배열을 오름차순 정렬하자 => java.util.Arrays
		
		Arrays.sort(ch);
		Arrays.sort(names);
		Arrays.sort(su);
		System.out.println("문자배열:"+Arrays.toString(ch));
		System.out.println("문자배열:"+Arrays.toString(names));
		System.out.println("정수배열:"+Arrays.toString(su));
		
		Integer [] su2 =  {13, 8, 7, 10, 100, 5};
		//su2 내림차순하기
		
		Arrays.sort(su2, Collections.reverseOrder());
		System.out.println("정수배열:"+Arrays.toString(su2));
		
	}
}
