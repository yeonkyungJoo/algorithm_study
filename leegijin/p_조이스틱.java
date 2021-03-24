package leegijin;

import java.util.ArrayList;

public class p_조이스틱 {

    public static void main(String[] args) {
        String name ="ZZZAZAA"; //111111111 ->9
        System.out.println(solution(name));
    }
    static public int solution(String name) {
        int answer = 0;

        int len = name.length();

        int min_move = len-1;

        for(int i=0; i<len; i++) {
            answer += Math.min(name.charAt(i)-'A', 'Z'-name.charAt(i)+1);

            int next = i+1;

            while(next<len && name.charAt(next) == 'A')
                next++;

            min_move = Math.min(min_move, i+len-next + i);
        }
        answer += min_move;

        return answer;
    }
}
