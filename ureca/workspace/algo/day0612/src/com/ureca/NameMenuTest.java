package com.ureca;

import java.util.Scanner;

public class NameMenuTest {

	public static void main(String[] args) {
		// 화면 출력
		// 사용자 데이터 입력
		Scanner scan = new Scanner(System.in);
		NameMenu menu = new NameMenu();
		// sc.nextInt() sc.nextDouble() sc.next() ==> whiteSpace를 구분자로 데이터를 입력
		// 정수입력 실수입력 문자열

		// sc.nextLine() ==> 라인(줄)을 구분자로
		int no;
		do {
			System.out.print("<이름메뉴>\r\n" + "1.추가 2.검색 3.수정 4.삭제 5.종료\r\n" + "번호입력 ==>");
			no = scan.nextInt();
			switch (no) {
			case 1: {
				System.out.print("이름입력: ");
				String name = scan.next();
				menu.create(name);
				break;
			}
			case 2: {
				String[] names = menu.read();
				System.out.println("#이름목록");
				for (String name : names) {
					if (name != null)
						System.out.println(" " + name);
				}
				break;
			}
			case 3:
				System.out.print("기존이름 입력:");
				String oldName = scan.next();
				System.out.print("변경이름 입력:");
				String newName = scan.next();
				menu.update(oldName, newName);
				break;
			case 4:
				System.out.print("삭제이름 입력:");
				String delName = scan.next();
				menu.delete(delName);
				break;
			} //switch 
			System.out.println();
		} while (no != 5);// (no<5)
		System.out.println("--END--");
		scan.close(); // 입력객체 반환
	}//main

}
