package com.ureca;

public class NameMenu {
	// 데이터에 대한 CRUD

	// 데이터 저장소
	String[] names = new String[5];

	void create(String name) {
		for (int i = 0; i < names.length; i++) {
			if (names[i] == null){//빈곳 찾기
				names[i] = name;
				break;// 자기를 포함한 영역을 벗어나는것, break는 루프와 switch case에서 쓰이는데
				//이를 벗어날때 사용된다.
			}
		}//for
	}//create

	String[] read() {//리턴타입이 String 타입의 배열
		return names;
	}

	void update(String oldName, String newName) {
		for(int i=0; i<names.length; i++) {
//			if(names[i]== oldName)) {// 변경할 이름을 찾았다면
			///==> String 메모리 주소 비교
			
				if(names[i].equals(oldName)) {
					//==> String(문자열) 내용 비교
				names[i]= newName;
				break;
			}
		}
	}

	void delete(String delName) {
		for(int i=0; i<names.length; i++) {
			if(names[i].equals(delName)) {
				names[i]=null;
				break;
			}
		}
	}
}
