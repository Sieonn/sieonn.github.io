package com.ureca;

import java.util.Arrays;
import java.util.Collections;

class Person implements Comparable<Person>{
	String name;
	int age;
	String job;
	int score;
	
	public Person() {
		// TODO Auto-generated constructor stub
	}

	public Person(String name, int age, String job, int score) {
		super();
		this.name = name;
		this.age = age;
		this.job = job;
		this.score = score;
	}

//	@Override
//	public String toString() {
//		return "\n[name=" + name + ", age=" + age 
//				+ ", job=" + job + ", score=" + score + "]";
//	}
	
	

	//==> Person이름의 오름차순 정렬하시오.
	@Override
	public int compareTo(Person o) {//
		//this(Person)의 속성과 o(Person)의 속성을 비교
		//비교방법  this.속성 -  o.속성
		//결과: 음수, 0, 양수  ==> 음수의 경우 swap을 해줌  ==> 오름차순 정렬
		
//		return this.age - o.age; //오름차순정렬
//		return this.name - o.name;
		return this.name.compareTo(o.name); //문자열의 경우는 오버라이드 메서드 사용
//		return 0;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("\n Person [name=");
		builder.append(name);
		builder.append(", age=");
		builder.append(age);
		builder.append(", job=");
		builder.append(job);
		builder.append(", score=");
		builder.append(score);
		builder.append("]");
		return builder.toString();
	}
	
	
	
	
}


public class ArraySortTest2 {
   public static void main(String[] args) {

	   int[]su= {13, 8, 7, 10, 100, 5};
	   char[]ch= {'J','a','v','A'};
	   String[]names= {"홍길동","길라임","김주원"};
	   
	   //API를 통해 배열을 오름차순 정렬하자~!! => java.util.Arrays	   
	   Arrays.sort(su);
	   Arrays.sort(ch);
	   Arrays.sort(names);
	   
	   System.out.println("정수배열>>"+ Arrays.toString(su));
	   System.out.println("문자배열>>"+ Arrays.toString(ch));
	   System.out.println("문자열배열>>"+ Arrays.toString(names));
	   
	   
	   Integer[]su2= {13, 8, 7, 10, 100, 5};
	   //su2배열을 내림차순 정렬하자!!
	   
	   Arrays.sort(su2, Collections.reverseOrder());
	   System.out.println("su2정수배열>>"+ Arrays.toString(su2));

	   
	   Person p = new Person("갓길동",11,"학생",95);
	   Person[] persons= {p ,
	      	            new Person("빛길동",19,"학생",80),
	   	            new Person("남길동",14,"학생",100),
	   	            new Person("여길동",17,"학생",99),
	   	            new Person("킹길동",15,"학생",56)};
	   
	    Arrays.sort(persons);   
	    
	    System.out.println(persons);//배열의 주소 출력
	    System.out.println(Arrays.toString(persons));//배열의 값을 문자열 형태로 출력

   }//main
}






