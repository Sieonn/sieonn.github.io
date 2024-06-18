package com.ureca.pack2;

import com.ureca.pack1.Parent;
public class Other {
	void callTest() {
		Parent p =new Parent();
		p.m1();
//		p.m2();
//		p.m3();
//		p.m4(); //존재는 하지만 보여지지 않는다 왜냐하면 private기 때문에
		
	}
}
