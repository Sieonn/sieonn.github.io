package com.ureca;

class A {
	public void happy() {
		System.out.println("즐거우세요? 아 즐거우시냐고요ㅎ");
	}
}//class A

class Child extends A{//=>클래스 시작 괄호
	@Override
	public void happy() {
		System.out.println("행복 찾기(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧");
	}
}//=>클래스 끝 괄호

interface Ureca{
	void good();
}
class My{
	public static void go(Ureca u) {
		u.good();
	}
}

class UrecaJunior implements Ureca
{//※※※

	@Override
	public void good() {
		System.out.println("응~ 최고다~");
	}
	
}//※※
public class AnonymousInnerClassTest {

	public static void main(String[] args) {
//		My.go(new Ureca()); 인터페이스는 객체화할 수 없어서 자식 클래스를 만들어줌
		My.go(new UrecaJunior());
		
		//자식클래스 없이 구현객체를 익명의 내부 클래스로 정의할 수 있음
		//==> 클래스 파일을 따로 만들지 않아도 되는 이점을 가졌음.
		My.go(new Ureca() {
			//※ 의미: 무명 implements Ureca
			@Override
			public void good() {
				System.out.println("졸려서 기절직전~~~");
			}//※※
			
		});
//		A a = new Child();//new A();
		A a = new Child() {/*내부클래스 영역*/
			public void happy() {
				System.out.println("졸려 죽겠다.");
			}
		};
		a.happy();
	}

}


