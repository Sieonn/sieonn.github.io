package test;

import java.util.Scanner;

public class Main_BJ_14681 {

	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		int x = sc.nextInt();
//		int y = sc.nextInt();
//		if (x > 0 && y > 0) 
//			System.out.println(1);
//		 else if (x > 0 && y < 0) 
//			System.out.println(4);
//		 else if (x < 0 && y > 0) 
//			System.out.println(2);
//		 else
//			System.out.println(3);
//		
//		sc.close();
		
		// 런타임 에러
		
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		int b = scanner.nextInt();

		if (a > 0 && b > 0) {
			System.out.println("1");
		} else if (a < 0 && b > 0) {
			System.out.println("2");
		} else if (a < 0 && b < 0) {
			System.out.println("3");
		} else if (a > 0 && b < 0) {
			System.out.println("4");
		}
	}

}
