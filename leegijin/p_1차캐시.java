package leegijin;

import java.util.LinkedList;
import java.util.Queue;

public class p_1차캐시 {
    public static void main(String[] args) {
        int cacheSize = 3;
        String [] cities = {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"};
        System.out.println(solution(cacheSize,cities));
    }
    public static int solution(int cacheSize, String[] cities) {
        int answer=0;
        if(cacheSize ==0)
            return cities.length*5;
        Queue<String> queue = new LinkedList<String>();
        for(String city : cities){
            String s = city.toLowerCase();
            if(queue.contains(s)){
                answer++;
                queue.remove(s);
                queue.add(s);
            }
            else{
                if(queue.size()<cacheSize) {
                    queue.add(s);
                }
                else {
                    queue.poll();
                    queue.add(s);
                }
                answer=answer+5;
            }

        }
        return answer;
    }
}
