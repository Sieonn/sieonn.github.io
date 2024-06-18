package com.lguplus;

public class ArrayTest5 {
	public static void main(String[] args) {
		int [] su ={1,2,3,4,5};
		for(int i=0; i<su.length; i++){
			System.out.print(su[4-i] + " ");
		}
		System.out.println();
		int [] su2 = new int[5];
		for(int i=0; i<su.length; i++){
			su2[i] = su[i];
			System.out.print(su2[i]+" ");
		}
		su2[0] = su[4];
		su2[4] = su[0];
		su2[1] = su[3];
		su2[3] = su[1];
		System.out.println();
		for(int i =0; i<su2.length; i++) {
			System.out.print( su2[i] +" ");
		}
	}
}
			