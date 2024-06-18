package com.uplus;

import java.io.BufferedReader;
import java.util.Scanner;

public class DoWhileTest {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		 int no = 0;
		 int num = 0;
		do {
	          System.out.println("1.검색 2.증가 3.감소 4.종료");
	          System.out.println("번호==> ");
	            no = sc.nextInt();
//	            BufferedReader br => Integer.parseInt(br.readLine());
	            switch (no) {
                case 1:
                    System.out.println("검색결과: "+ num );
                    break;
                case 2:
                	num +=1;
                    System.out.println("1증가하였습니다.");
                    break;
                case 3:
                	num -= 1;
                    System.out.println("1감소하였습니다.");
                    break;
                case 4:
                    System.out.println("-END-");
                    break;
                default:
                    System.out.println("잘못된 입력입니다. 다시 입력해주세요.");
            }
        } while (no != 4);
        sc.close();
    }
}

//