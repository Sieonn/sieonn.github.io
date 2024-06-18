import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_BJ_12891_DNA비밀번호2 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        int s = Integer.parseInt(st.nextToken()); // 민호가 만든 문자열의 길이
        int p = Integer.parseInt(st.nextToken()); // 비밀번호로 사용할 부분문자열의 길이

        String password = br.readLine(); // CCTGGATTG

        String partStrNum = br.readLine(); // 2 0 1 1
        StringTokenizer st2 = new StringTokenizer(partStrNum, " ");
        int[] numArray = new int[4];
        for (int i = 0; i < 4; i++) {
            numArray[i] = Integer.parseInt(st2.nextToken());
        }

        int result = 0;

        for (int i = 0; i <= s - p; i++) {
            String subStr = password.substring(i, i + p);
            int[] count = new int[4];

            for (int j = 0; j < p; j++) {
                char ch = subStr.charAt(j);
                if (ch == 'A') count[0]++;
                else if (ch == 'C') count[1]++;
                else if (ch == 'G') count[2]++;
                else if (ch == 'T') count[3]++;
            }

            boolean isValid = true;
            for (int k = 0; k < 4; k++) {
                if (count[k] < numArray[k]) {
                    isValid = false;
                    break;
                }
            }

            if (isValid) {
                result++;
            }
        }

        System.out.println(result);
    }
}
