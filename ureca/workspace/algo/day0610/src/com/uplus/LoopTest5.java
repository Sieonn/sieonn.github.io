package com.uplus;

public class LoopTest5 {
	public static void main(String[] args) {
		System.out.print("[");
		for(int i =5; i<21; i+=5) {
			System.out.print(i);
			if(i<20)
			System.out.print(", ");
		}
		System.out.print("]");
	}
}
