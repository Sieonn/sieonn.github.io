import java.util.Scanner;

public class Main_BJ_1000_AB2 {

	public static void main(String[] args) {
		//입력도구: scanner, BufferedReader
		// A a = new A(); ===> A클래스의 멤버를 사용할 준비
		Scanner scan = new Scanner(System.in); //===> 스캐너 클래스의 멤버를 사용할 준비
		
		//입력 데이터 => 1 2
//		int su1=scan.nextInt(); //next는 데이터 가져오기(끌어오기)이다.
//		int su2=scan.nextInt(); //next는 데이터 가져오기(끌어오기)이다.
		
		
		//변수에 저장하는 값은 또 사용해야할 때 사용하는데, 한번 사용하고 말것이면 직접 출력해도 된다.
		
		System.out.println(scan.nextInt()+scan.nextInt());
		
		scan.close();//입출력 객체는 자원 반환하는 것이 기본이다.
	}//main

}
