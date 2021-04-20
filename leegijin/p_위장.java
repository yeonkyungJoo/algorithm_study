package leegijin;

import java.util.HashMap;

public class p_위장 {
    public static void main(String[] args) {
        String[][] clothes  = {{"yellow_hat", "headgear"},{"blue_sunglasses", "eyewear"},{"green_turban", "headgear"}};
        System.out.println(solution(clothes));
    }
    public static int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int answer = 0;
        for(String[] t : clothes){
            int cnt =1;
            if(map.containsKey(t[1])){
                cnt=map.get(t[1])+1;
            }
            map.put(t[1],cnt);
        }
        int cnt=1;
        for(String key : map.keySet()){
            cnt=cnt*(map.get(key)+1);
        }
        answer=cnt-1;
        return answer;
    }
}
