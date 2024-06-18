package day0612;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class ArrayTest {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		String[] names = new String[5];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str;
		String str2;
		int no;
		do {
			System.out.println("1.추가 2.검색 3.수정 4.삭제 5.종료");
			System.out.print("번호==> ");
//	            String num = br.readLine();
//	            int no = Integer.parseInt(num);
			no = sc.nextInt();
			switch (no) {
			case 1:
				System.out.print("이름입력: ");
				str = br.readLine();
				for (int i = 0; i < 5; i++) {
					if (names[i] == null) {
						names[i] = str;
						break;
					}
				}
				break;
			case 2:
				System.out.println("#이름목록");
				for (int i = 0; i < 5; i++) {
					if (names[i] != null) {
						System.out.println(names[i]);
					}
				}
				break;
			case 3:
				System.out.print("기존이름 입력: ");
				str = br.readLine();
				System.out.print("변경이름 입력: ");
				str2 = br.readLine();
				for (int i = 0; i < 5; i++) {
					if (str.equals(names[i])) {
						names[i] = str2;
					}
				}
				break;
			case 4:
				System.out.print("삭제이름 입력: ");
				str = br.readLine();
				for(int i=0; i<5; i++) {
					if(str.equals(names[i])) {
						names[i]= null;
						break;
					}
				}
				break;
			case 5:
				System.out.println("--END--");
				break;
			default:
				System.out.println("잘못된 입력입니다. 다시 입력해주세요.");
			}
		} while (no != 5);
		sc.close();
	}
}