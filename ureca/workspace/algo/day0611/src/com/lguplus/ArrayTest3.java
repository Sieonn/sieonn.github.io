package com.lguplus;

public class ArrayTest3 {
	public static void main(String[] args) {
		int su2[][]={ {1}, {1,2}, {1,2,3}};
		for(int i= 0; i<su2.length; i++) {
			for(int j=0; j<su2[i].length; j++) {
				System.out.println("su2["+i+"]"+"["+j+"]번지 = "+ su2[i][j]);
			}
		}
	}
}
			