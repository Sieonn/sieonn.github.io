
public class A {

	public static void main(String[] args) {

		String str="ABC";
		String [] strArr = {"D", "E", "F"};
		for(int i =0; i<3; i++) {
			str+=strArr[i];
		}
		System.out.println(str);
	}

}
