package Mission;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
class L{
	public Collection<? extends String> lottoGen() {
		int[] randomNum = new int[6];
		for (int i = 0; i < 6; i++) {
			int newNum;
			do {
				newNum = (int) (Math.random() * 45) + 1;
			} while (contains(randomNum, newNum));
			randomNum[i] = newNum;
		}
		System.out.println(Arrays.toString(randomNum));
		return null;
	}

	private static boolean contains(int[] randomNum, int newNum) {
		for (int su : randomNum) {
			if (su == newNum) {
				return true;
			}
		}
		return false;
	}
}
public class LottoTest {

	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<>();

		 L lot = new L();
		 list.addAll(lot.lottoGen());
		 
		
	}
}
