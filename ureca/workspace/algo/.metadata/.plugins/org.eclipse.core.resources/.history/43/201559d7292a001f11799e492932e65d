package Mission;

import java.util.Arrays;

public class Lotto {
	public void LottoGen() {
		int[] randomNum = new int[6];
		for (int i = 0; i < 6; i++) {
			int newNum;
			do {
				newNum = (int) (Math.random() * 45) + 1;
			} while (contains(randomNum, newNum));
			randomNum[i] = newNum;
		}
		System.out.println(Arrays.toString(randomNum));
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
