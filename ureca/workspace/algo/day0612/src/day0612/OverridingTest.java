package day0612;

import java.util.ArrayList;
import java.util.Vector;

public class OverridingTest {

	public static void main(String[] args) {

		// 가변배열
//		ArrayList list1 = new ArrayList();//데이터를 입력을하면 사이즈가 알아서 할당된다. ==>Object를 입력
//		ArrayList<String> list1 = new ArrayList<String>();//제네릭타입 ==> 특정 데이터타입 명시
		ArrayList<String> list1 = new ArrayList<>();// 제네릭타입 ==> 특정 데이터타입 명시
		list1.add("홍길동");
		list1.add("길라임");
		list1.add("김주원");
//			list1.add(1004); //타입이 일치하지 않아서 오류남

		My2.print(list1);
		
		System.out.println("=============================");
		
		Vector<String> list2 = new Vector<>();
			list2.add("야구");
			list2.add("축구");
			list2.add("배구");
			
		My2.print(list2);
		
		//ArrayList<String>과 Vector<String>은 List의 자식들이여서 에러가 안남
	}// main

}
