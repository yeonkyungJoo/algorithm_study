package leegijin;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class p_영어끝말잇기 {

    public static void main(String[] args) {
        String[] a = new String[]{"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"};
        String[] b = new String[]{"hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang","gather", "refer", "reference", "estimate", "executive"};
        String[] d = new String[]{"hello", "one", "even", "never", "now", "world", "draw"};
        int n = 3;
        int[] c = solution(n,a);
        System.out.println(Arrays.toString(c));
    }
    public static int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Map<String, Integer> checkList = new HashMap<String, Integer>();
        checkList.put(words[0], 0);
        for(int i=0;i<words.length-1;i++){

            String x =words[i].substring(words[i].length()-1);
            String y = words[i+1].substring(0, 1);

            if(!x.equals(y) || checkList.containsKey(words[i+1])){

                if((i+2)%n==0){
                    answer[0] = n;
                    answer[1] =    (i+2)/n;
                    return answer;
                }else{
                    answer[0] = (i+2)%n;
                    answer[1] =    ((i+2)/n)+1;
                    return answer;
                }

            }
            else{
                checkList.put(words[i+1], i+1);
                answer[0]=0;
                answer[1]=0;
            }
        }
        return answer;
    }


}

