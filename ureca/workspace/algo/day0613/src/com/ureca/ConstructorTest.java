package com.ureca;

public class ConstructorTest {

	public static void main(String[] args) {
		Abc a =  new Abc();
		a.hello();
		
		System.out.println("a.str="+ a.str);
				
		Abc a2 =new Abc("Java");
		System.out.println("a2.str="+ a2.str);
	}

}
