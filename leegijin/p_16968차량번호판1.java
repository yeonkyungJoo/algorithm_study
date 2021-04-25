package leegijin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p_16968차량번호판1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        long answer = 1;
        
        for (int i = 0; i < s.length(); i++) {
            if(i==0) {
                if (s.charAt(i) == 'c')
                    answer = answer * 26;
                else
                    answer = answer * 10;
            }
            else
                if(s.charAt(i-1)==s.charAt(i)) {
                    if (s.charAt(i) == 'c')
                        answer = answer * 25;
                    else
                        answer = answer * 9;
                }
                else
                    if (s.charAt(i) == 'c')
                        answer = answer * 26;
                    else
                        answer = answer * 10;
        }
        System.out.println(answer);
    }
}
