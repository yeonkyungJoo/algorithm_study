package leegijin;

import java.util.ArrayList;
import java.util.Arrays;

public class p_3차압축 {
    public static void main(String[] args) {
        String s ="TOBEORNOTTOBEORTOBEORNOT";
        int tmp [] = solution(s);
        for(int t : tmp){
            System.out.println("t = " + t);
        }
    }

    public static int[] solution(String msg) {
        String [] alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
        ArrayList<String> index = new ArrayList<>(Arrays.asList(alpha));
        if (msg.length() == 1) {
            int i = index.indexOf(msg);
            return new int[] {i+1};
        }

        ArrayList<Integer> ans = new ArrayList<>();
        int idx = 1;
        String s = ""+msg.charAt(0);

        while(idx <= msg.length()) {

            if (idx == msg.length()) {
                ans.add(index.indexOf(s)+1);
                break;
            }

            char c = msg.charAt(idx);
            String wc = s+c;

            if (index.contains(wc)) {
                s = wc;
                idx++;
                continue;
            }

            index.add(wc);
            ans.add(index.indexOf(s)+1);
            s = ""+c;
            idx++;

        }
        int[] answer = new int[ans.size()];
        for (int i = 0; i < answer.length; i++) answer[i] = ans.get(i);
        return answer;
    }
}