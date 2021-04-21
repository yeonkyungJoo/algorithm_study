package leegijin;

import java.util.LinkedList;
import java.util.Queue;

public class p_다리를지나는트럭 {
    class Info{
        private int weight ;
        private int time;

        public Info(int weight, int time) {
            this.weight = weight;
            this.time = time;
        }
    }
    public static void main(String[] args) {
        int bridge_length =2;
        int weight =10;
        int [] truck_weights = {7,4,5,6};
        p_다리를지나는트럭 a = new p_다리를지나는트럭();
        int answer = a.solution(bridge_length,weight,truck_weights);
        System.out.println("answer = " + answer);
    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        // truck 다리위에 있는 트럭과 대기 하고 있는 트럭 구현 필요
        // 다리위에있는 트럭을 큐로 구현해서 검사해서 들갈수있게
        Queue <Integer> queue = new LinkedList<>();
        Queue <Info> bridge = new LinkedList<>();

        for(int tmp : truck_weights){
            queue.add(tmp);
        }
        int cnt=0;
        while(!queue.isEmpty()){
            int tmp =0;
            cnt++;
            if(!bridge.isEmpty()) {
                if (cnt - bridge.peek().time == bridge_length)
                    weight = weight+bridge.poll().weight;
            }
            if(weight>=queue.peek()) {
                tmp = queue.poll();
                bridge.add(new Info(tmp,cnt));
                weight=weight-tmp;
            }
        }
        return cnt+bridge_length;
    }
}
