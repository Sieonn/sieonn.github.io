import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_BJ_1000_AB {

	public static void main(String[] args) throws Exception {
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine(); //str ="1 2"
		
		StringTokenizer tokens =  new StringTokenizer(str," ");	
						//tokens = ["1", "2"]
		
		int su1 = Integer.parseInt(tokens.nextToken()); //"1" //Integer.paeeInt("1") > 1
		int su2 = Integer.parseInt(tokens.nextToken()); //"2" //Integer.paeeInt("2") > 2
		
		System.out.println(su1+su2);
			
	}//main
	//스캐너를 사용해도 되지만 BufferedReader가 더 빠르다

}
