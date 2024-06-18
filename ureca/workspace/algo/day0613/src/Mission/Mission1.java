package Mission;

import java.util.Arrays;

public class Mission1 {
	public static void main(String[] args) {
		int [] su = {13, 8, 7, 10, 100, 5};
//		Arrays.sort(su);
//		System.out.println(Arrays.toString(su));
		int temp;
		for( int i =0; i<su.length-1;i++) {
			for(int j = i+1; j<su.length; j++) {
				if(su[i] > su[j]) {
					temp = su[i];
					su[i] = su[j];
					su[j] = temp;
				}
			}
		}
		//정렬된 
		System.err.println(Arrays.toString(su));
	}//main
}
